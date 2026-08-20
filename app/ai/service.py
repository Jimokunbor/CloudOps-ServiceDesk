from app.ai.config import AIConfig
from app.ai.providers import (
    AIProvider,
    AzureOpenAIProvider,
    BedrockProvider,
    OllamaProvider,
    OpenAIProvider,
)
from app.ai.schemas import AIResponse


class AIService:
    def __init__(self):
        self.provider = self._load_provider()

    def _load_provider(self) -> AIProvider:
        provider = AIConfig.PROVIDER.lower()

        if provider == "openai":
            return OpenAIProvider()

        if provider == "azure":
            return AzureOpenAIProvider()

        if provider == "ollama":
            return OllamaProvider()

        if provider == "bedrock":
            return BedrockProvider()

        raise ValueError(f"Unsupported AI provider: {provider}")

    def generate(
        self,
        prompt: str,
    ) -> AIResponse:
        response = self.provider.generate(prompt)

        return AIResponse(
            provider=AIConfig.PROVIDER,
            model=AIConfig.MODEL,
            response=response,
            success=True,
        )