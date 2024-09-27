from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

from typing import Any

class Settings(BaseSettings):
    bot_token: SecretStr

    admin_id: int
    channel_id: int

    anekdot_time: Any
    night_time: Any

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
