"""Webapp main function."""

from io import StringIO
from pathlib import Path
from typing import Dict

import uvicorn
from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.html_exporter import HTMLExporter
from ontogpt.io.template_loader import get_template_details

this_path = Path(__file__).parent
static_dir = this_path / "static"
html_dir = this_path / "html"

DATAMODELS = [
    "biological_process.BiologicalProcess",
    "biotic_interaction.BioticInteraction",
    "cell_type.CellTypeDocument",
    "condition",
    "ctd.ChemicalToDiseaseDocument",
    "data_sheets_schema",
    "diagnostic_procedure.DiagnosticProceduretoPhenotypeAssociation",
    "dietitian_notes",
    "drug.DrugMechanism",
    "emapa_simple",
    "environmental_sample.Study",
    "figure",
    "go_simple",
    "gocam.GoCamAnnotations",
    "mendelian_disease.MendelianDisease",
    "maxo",
    "mondo_simple",
    "phenotype.Trait",
    "reaction.Reaction",
    "recipe.Recipe",
    "treatment.DiseaseTreatmentSummary",
]

LLM_MODELS = ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"]


class Query(BaseModel):
    text: str
    datamodel: str
    model: str


app = FastAPI()
static_dir.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
templates = Jinja2Templates(directory=str(html_dir))

html_exporter = HTMLExporter(output=None)
engines: Dict[str, SPIRESEngine] = {}


def get_engine(datamodel: str, llm_model: str):
    if datamodel not in engines:
        template_details = get_template_details(template=datamodel)
        try:
            engines[datamodel] = SPIRESEngine(
                model=llm_model, template_details=template_details, model_source="openai"
            )
        except ValueError as e:
            print(f"Encountered an error setting up the knowledge engine: {e}")
            print("Will fall back to defaults.")
            engines[datamodel] = SPIRESEngine(
                model="gpt-3.5-turbo", template_details=template_details, model_source="openai"
            )
    return engines[datamodel]


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        "form.html",
        context={"request": request, "datamodels": DATAMODELS, "llm_models": LLM_MODELS},
    )


@app.post("/")
def form_post(
    request: Request, datamodel: str = Form(...), text: str = Form(...), llm_model: str = Form(...)
):
    print(f"Received request with schema {datamodel}")
    print(f"Received request with text {text}")
    print(f"Received request to be sent to {llm_model}")
    engine = get_engine(datamodel, llm_model)
    ann = engine.extract_from_text(text)
    print(f"Got {ann}")
    output = StringIO()
    html_exporter.export(extraction_output=ann, output=output)
    return templates.TemplateResponse(
        "results.html", context={"request": request, "inner_html": output.getvalue()}
    )


def start():
    """Launch with `poetry run start` at root level."""
    uvicorn.run("ontogpt.webapp.main:app", host="127.0.0.1", port=8000, reload=True)
