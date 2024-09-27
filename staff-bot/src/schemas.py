from common.schemas import UserBase
from pydantic import BaseModel

from common.models import DonorStatusEnum


class ChangeDonorStatusRequestSchema(BaseModel):
    id : int
    donor_status : DonorStatusEnum

class ShowDonorInfoToVolunteerSchema(UserBase):
    id : int
    donor_status : DonorStatusEnum