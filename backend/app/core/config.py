from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Moven API"
    DEBUG: bool = True
    VERSION: str = "0.1.0"

    DATABASE_URL: str = "postgresql+asyncpg://localhost:5432/moven"
    REDIS_URL: str = "redis://localhost:6379/0"

    ANTHROPIC_API_KEY: str = ""

    JWT_SECRET: str = "change-me-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 60 * 24  # 1 day

    class Config:
        env_file = ".env"


settings = Settings()
