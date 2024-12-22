from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    api_key: str = Field(default='api_key', alias='API_KEY')


settings = Config()
