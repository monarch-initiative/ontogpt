"""Topic classifier engine."""

from dataclasses import dataclass

from ontogpt.engines.knowledge_engine import KnowledgeEngine


@dataclass
class TopicClassifierEngine(KnowledgeEngine):
    """Engine for classifying input text based on its topic."""

    def binary_classify(self, topic: str, text: str) -> bool:
        """Given a topic description, indicate whether it applies to the input text."""

        prompt = (
            "I will provide a topic followed by a text."
            " If the text matches the topic, return only 'True'."
            " If the text does not match the topic, return only 'False'."
            " Do not provide any other text."
            f" Topic: {topic}"
            f" Text: {text}"
        )
        payload = self.client.complete(prompt)
        if payload.lower in ["true"]:
            return True
        else:
            return False
