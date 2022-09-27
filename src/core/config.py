import os
import pytz
from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = '0.0.0.0'
    port: int = 6000

    SECRET_KEY = "abd6e3e21d6c99696c91b9c1a08783e4c45de4e3901d58ece33a2ad992abfaa7"
    DATABASE_URL = "postgres://{}:{}@{}/{}".format(os.getenv("DB_USER"),
                                                   os.getenv("DB_PASS"),
                                                   os.getenv("DB_HOST"),
                                                   os.getenv("DB_NAME"))
    API_V1_STR: str = "/api/v1"
    BASE_DIR: str = "/app/"
    USER_PASSWORD_LENGTH: int = 6
    MOSCOW_TZ = pytz.timezone('Europe/Minsk')

    APPS_MODELS = [
        "aerich.models",
        "models.address",
        "models.citybike_stations"
    ]

    class Config:
        case_sensitive = True


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
