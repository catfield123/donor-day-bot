from datetime import date, datetime

from common.schemas import UserBase
from common.models import DonorStatusEnum, FoundingSourceEnum, SexEnum, BodyWeightEnum
from pydantic import EmailStr, BaseModel, field_validator

class UserCreate(UserBase): 
    phone_number : str
    email: EmailStr

    is_polytech_student : bool
    grade_book_number : str = None
    group_number : str = None
    faculty_id : int = None
    founding_source : FoundingSourceEnum | None = None

    inn : str
    snils : str

    passport_series : str
    passport_number : str
    passport_issued_by : str
    passport_issued_date : date
    passport_issued_organization_code : str

    birth_date : date
    birth_place : str
    registration_address : str

    sex : SexEnum
    body_weight : BodyWeightEnum
    bone_marrow_typing_agreement : bool

    donation_place : str
    donation_datetime : datetime

    donor_status : DonorStatusEnum = DonorStatusEnum.not_specified

class UserShow(UserCreate): 
    id : int

class DonationPlaceDbResponse(BaseModel):
    id: int
    name: str

class DonationDatetimesDbResponse(BaseModel):
    id: int
    place_id: int
    datetime: str

    @field_validator("datetime", mode="before")
    def validate_datetime(cls, value):
        return value.strftime("%d.%m.%Y %H:%M")
