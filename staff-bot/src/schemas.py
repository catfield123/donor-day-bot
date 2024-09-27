from common.schemas import UserBase
from pydantic import BaseModel

from common.models import DonorStatusEnum

class NewVolunteerRequestSchema(BaseModel):
    telegram_id : str
    granted_by_telegram_id : str

class ChangeDonorStatusRequestSchema(BaseModel):
    id : int
    donor_status : DonorStatusEnum

class ShowDonorInfoToVolunteerSchema(UserBase):
    id : int
    donor_status : DonorStatusEnum