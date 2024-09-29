
from sqlalchemy.orm import Session
from common.models import Faculty

def db_get_faculties_names(db: Session):
    return [faculty.name for faculty in db.query(Faculty).all()]