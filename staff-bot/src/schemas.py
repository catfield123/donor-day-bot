from common.schemas import UserBase
from pydantic import BaseModel

from common.models import DonorStatusEnum


class ChangeDonorStatusRequest(BaseModel):
    id : int
    donor_status : DonorStatusEnum

class ShowDonorInfoToVolunteer(UserBase):
    id : int
    donor_status : DonorStatusEnum