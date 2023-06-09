"""Reasoner engine."""
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from jinja2 import Template
from oaklib import get_adapter
from oaklib.datamodels.text_annotator import TextAnnotationConfiguration
from oaklib.interfaces import MappingProviderInterface, TextAnnotatorInterface
from pydantic import BaseModel

from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.prompts.phenopacket import DEFAULT_PHENOPACKET_PROMPT

logger = logging.getLogger(__name__)


# TODO: use phenopacket python datamodel
PHENOPACKET = Dict[str, Any]
DIAGNOSIS = Dict[str, Any]


class DiagnosisPrediction(BaseModel):
    case_id: str
    validated_disease_ids: List[str] = None
    validated_disease_labels: List[str] = None
    validated_mondo_disease_ids: List[str] = None
    validated_mondo_disease_labels: List[str] = None
    predicted_disease_ids: List[str] = None
    predicted_disease_labels: List[str] = None
    matching_disease_ids: List[str] = None
    rank: Optional[int] = None
    model: Optional[str] = None
    prompt: Optional[str] = None


@dataclass
class PhenoEngine(KnowledgeEngine):
    completion_length = 850
    _mondo: TextAnnotatorInterface = None

    @property
    def mondo(self):
        if not self._mondo:
            self._mondo = get_adapter("sqlite:obo:mondo")
        return self._mondo

    def predict_disease(
        self, phenopacket: PHENOPACKET, template_path: Union[str, Path] = None
    ) -> List[DIAGNOSIS]:
        if template_path is None:
            template_path = DEFAULT_PHENOPACKET_PROMPT
        if isinstance(template_path, Path):
            template_path = str(template_path)
        if isinstance(template_path, str):
            # create a Jinja2 template object
            with open(template_path) as file:
                template_txt = file.read()
                template = Template(template_txt)
        prompt = template.render(
            phenopacket=phenopacket,
        )
        payload = self.client.complete(prompt, max_tokens=self.completion_length)
        print(payload)
        try:
            obj = json.loads(payload)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {e}")
            logger.error(f"Payload: {payload}")
            obj = []
        self.enhance_payload(obj)
        return obj

    def evaluate(self, phenopackets: List[PHENOPACKET]) -> List[DiagnosisPrediction]:
        mondo = self.mondo
        if not isinstance(mondo, MappingProviderInterface):
            raise TypeError("Mondo adapter must implement MappingProviderInterface")

        results = []
        for phenopacket in phenopackets:
            dp = DiagnosisPrediction(case_id=phenopacket["id"], model=self.model)
            validated_disease_ids = {disease["term"]["id"] for disease in phenopacket["diseases"]}
            dp.validated_disease_ids = list(validated_disease_ids)
            dp.validated_disease_labels = [
                disease["term"]["label"] for disease in phenopacket["diseases"]
            ]
            dp.validated_mondo_disease_ids = []
            dp.validated_mondo_disease_labels = []
            for disease_id in validated_disease_ids:
                mondo_id = mondo.normalize(disease_id, target_prefixes=["MONDO"])
                if mondo_id:
                    dp.validated_mondo_disease_ids.append(mondo_id)
                    dp.validated_mondo_disease_labels.append(mondo.label(mondo_id))
                else:
                    logger.warning(f"Could not normalize {disease_id} to MONDO")
            diagnoses = self.predict_disease(phenopacket)
            dp.predicted_disease_ids = []
            dp.predicted_disease_labels = []
            dp.rank = 999
            for i, diagnosis in enumerate(diagnoses):
                predicted_disease_ids = diagnosis["disease_ids"]
                dp.predicted_disease_ids.append(";".join(predicted_disease_ids))
                dp.predicted_disease_labels.append(diagnosis["disease"])
                matches = set(dp.validated_mondo_disease_ids).intersection(predicted_disease_ids)
                if matches:
                    print("Found match at index", i)
                    dp.rank = i
                    dp.matching_disease_ids = list(matches)
                    break
            print(dump_minimal_yaml(dp.dict()))
            results.append(dp)
        return results

    def enhance_payload(self, diagnoses: List[DIAGNOSIS]) -> List[DIAGNOSIS]:
        """Enhance payload with additional information."""
        mondo = self.mondo
        config = TextAnnotationConfiguration(matches_whole_text=True)
        if not isinstance(mondo, TextAnnotatorInterface):
            raise ValueError("Mondo adapter must implement TextAnnotatorInterface")
        for diagnosis in diagnoses:
            disease_label = diagnosis["disease"]
            anns = list(mondo.annotate_text(disease_label, config))
            # print(anns)
            diagnosis["disease_ids"] = [ann.object_id for ann in anns]
        return diagnoses
