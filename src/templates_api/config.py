from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI template"

    class Config:
        env_file = ".env"


settings = Settings()
