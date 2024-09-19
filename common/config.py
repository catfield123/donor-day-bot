from pydantic_settings import BaseSettings
from pydantic import Field

class DatabaseSettings(BaseSettings):
    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_DB : str = Field(..., env="POSTGRES_DB")
    database_host: str = "db"
    database_port: str = "5432"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.database_host}:{self.database_port}/{self.POSTGRES_DB}"
        )

database_settings = DatabaseSettings()