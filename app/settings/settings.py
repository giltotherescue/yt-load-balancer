from enum import StrEnum

from pydantic_settings import SettingsConfigDict, BaseSettings


class EnvMode(StrEnum):
    DEV = "dev"
    PROD = "prod"


class ApiSettings(BaseSettings):
    API_KEY: str
    ENV: str = EnvMode.PROD
    SCRAPER_SERVICE_PREFIX: str = "proxy-scrapper"

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


api_settings = ApiSettings()
