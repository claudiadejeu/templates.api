from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI template"

    class ConfigDict:
        env_file = ".env"


settings = Settings()
