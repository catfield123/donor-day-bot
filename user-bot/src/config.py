from pydantic_settings import BaseSettings
from pydantic import Field

class UserSettings(BaseSettings):
    USER_BOT_TOKEN : str = Field(..., env="USER_BOT_TOKEN")

user_settings = UserSettings()