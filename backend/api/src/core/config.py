from pydantic import validator
from pydantic_settings import BaseSettings


# Get config values from env variables, see https://fastapi.tiangolo.com/advanced/settings/
# TODO: use lru_cache decorator
class Settings(BaseSettings):
    project_name: str = "sovai_authO"
    project_description: str = (
        "this is a central app that will handle user auth + subscription"
    )
    port: int = 9003

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

# print(settings)
