from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    COPILOT_API_BASE_URL: str = "https://owpublic.blob.core.windows.net/tech-task/"


settings = Settings()
