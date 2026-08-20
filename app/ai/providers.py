from abc import ABC
from abc import abstractmethod


class AIProvider(ABC):
    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response from the configured AI provider.
        """
        pass


class OpenAIProvider(AIProvider):
    def generate(
        self,
        prompt: str,
    ) -> str:
        return "OpenAI integration will be implemented in a later milestone."


class AzureOpenAIProvider(AIProvider):
    def generate(
        self,
        prompt: str,
    ) -> str:
        return "Azure OpenAI integration will be implemented in a later milestone."


class OllamaProvider(AIProvider):
    def generate(
        self,
        prompt: str,
    ) -> str:
        return "Ollama integration will be implemented in a later milestone."


class BedrockProvider(AIProvider):
    def generate(
        self,
        prompt: str,
    ) -> str:
        return "AWS Bedrock integration will be implemented in a later milestone."