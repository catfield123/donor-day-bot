from common.schemas import UserBase
from pydantic import BaseModel

from common.models import DonorStatusEnum

class UserChangeStatusRequest(BaseModel):
    id : int
    donor_status : DonorStatusEnum

class UserShowToVolunteer(UserBase):
    id : int
    donor_status : DonorStatusEnum