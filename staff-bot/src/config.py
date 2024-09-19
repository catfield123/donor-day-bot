from pydantic_settings import BaseSettings
from pydantic import Field

class StaffSettings(BaseSettings):
    STAFF_BOT_TOKEN : str = Field(..., env="STAFF_BOT_TOKEN")

staff_settings = StaffSettings()