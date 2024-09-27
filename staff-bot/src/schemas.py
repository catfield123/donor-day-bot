from common.schemas import UserBase
from pydantic import BaseModel, ConfigDict

from common.models import DonorStatusEnum

class CheckAuthRequestSchema(BaseModel):
    telegram_id : str
    
    model_config = ConfigDict(coerce_numbers_to_str=True)

class NewVolunteerRequestSchema(BaseModel):
    telegram_id : str
    granted_by_telegram_id : str

    model_config = ConfigDict(coerce_numbers_to_str=True)

class ChangeDonorStatusRequestSchema(BaseModel):
    id : int
    donor_status : DonorStatusEnum

    model_config = ConfigDict(coerce_numbers_to_str=True)

class ShowDonorInfoToVolunteerSchema(UserBase):
    id : int
    donor_status : DonorStatusEnum
    
    