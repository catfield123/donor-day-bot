from sqlalchemy.orm import Session
from common.models import Volunteer
from exceptions.new_volunteer import VolunteerAlreadyExists
from schemas import NewVolunteerRequestSchema

def create_new_volunteer(db: Session, new_volunteer_request: NewVolunteerRequestSchema) -> bool:
    existing_volunteer = db.query(Volunteer).filter(Volunteer.telegram_id == str(new_volunteer_request.telegram_id)).first()

    if existing_volunteer:
        raise VolunteerAlreadyExists
    
    db.add(Volunteer(telegram_id=str(new_volunteer_request.telegram_id), granted_by_telegram_id=str(new_volunteer_request.granted_by_telegram_id)))
    db.commit()
    return True