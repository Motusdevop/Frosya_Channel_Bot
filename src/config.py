from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    """
    Класс конфигурации для загрузки переменных окружения.
    Использует pydantic для удобного парсинга.
    """
    BOT_TOKEN: SecretStr
    ADMIN_ID: int
    CHAT_ID: int
    GOODNIGHT_TIME: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()