import logging

from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)


class Settings(BaseSettings):
    """App settings."""

    project_name: str = "alchemist"
    debug: bool = False
    environment: str = "local"

    # Database
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost/postgres"
    # database_url: str = "postgresql+psycopg://postgres:postgres@localhost/postgres"


settings = Settings()
