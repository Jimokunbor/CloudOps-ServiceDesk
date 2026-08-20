class AIProviderError(Exception):
    """Raised when an AI provider cannot process a request."""

    pass


class AIConfigurationError(Exception):
    """Raised when the AI configuration is invalid."""

    pass


class AIRequestError(Exception):
    """Raised when an AI request is invalid."""

    pass