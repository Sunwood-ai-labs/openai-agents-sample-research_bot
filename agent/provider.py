import os
from openai import AsyncOpenAI
from agents.model_settings import ModelSettings

def create_client(model_name: str = None) -> tuple[AsyncOpenAI, str]:
    """
    環境変数からモデル設定を読み込み、OpenAIクライアントとモデル名を返す

    Returns:
        tuple[AsyncOpenAI, str]: (OpenAIクライアント, モデル名)
    """
    base_url = os.getenv("OPENAI_API_BASE")
    api_key = os.getenv("OPENAI_API_KEY")
    default_model = os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo")

    client = AsyncOpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    return client, model_name or default_model

def create_model_settings(temperature: float = 0.7) -> ModelSettings:
    return ModelSettings(temperature=temperature)
