from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BACKEND_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
