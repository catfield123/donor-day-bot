from datetime import date, datetime
from typing_extensions import Self
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator

class UserBase(BaseModel):
    telegram_id : str

    name : str
    surname : str
    patronymic : str = None
