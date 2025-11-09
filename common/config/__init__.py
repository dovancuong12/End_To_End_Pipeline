from .config import Configs, EmbeddingConfigs, LlmConfigs, PostgresConfigs, AppConfigs, WebSearchConfigs

# Create a single instance of configs to be used throughout the application
configs = Configs()

__doc__ = "Configuration management for the application"

__all__ = [
    "configs",
    "Configs",
    "PostgresConfigs",
]