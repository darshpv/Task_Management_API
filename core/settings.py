from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_SYNC_URL: str
    APP_ENV: str
    LOG_LEVEL: str

    class Config:
        env_file = ".env"


settings = Settings()