from pydantic import BaseModel, field_validator

class UserBase(BaseModel):
    telegram_id : str

    name : str
    surname : str
    patronymic : str | None = None

    @field_validator("telegram_id", mode="before")
    def validate_telegram_id(cls, value):
        if value:
            return str(value)
    
