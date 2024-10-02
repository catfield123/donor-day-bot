from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from common.models import DonationDatetime, Faculty, DonationPlace, User

from schemas import DonationDatetimesDbResponse, DonationPlaceDbResponse, FacultyDbResponse, UserCreate, UserUpdate

from functools import lru_cache

@lru_cache
def db_get_faculties_names(db: Session) -> list[FacultyDbResponse]:
    return [FacultyDbResponse(id=faculty.id, name=faculty.name) for faculty in db.query(Faculty).all()]

@lru_cache
def db_get_donation_places(db: Session) -> list[DonationPlaceDbResponse]:
    return [DonationPlaceDbResponse(id=donation_place.id, name=donation_place.name) for donation_place in db.query(DonationPlace).all()]

@lru_cache
def db_get_donation_datetimes(db: Session, donation_place_id: int) -> list[DonationDatetimesDbResponse]:
    return [
        DonationDatetimesDbResponse(id=donation_datetime.id, place_id = donation_datetime.place_id,datetime=donation_datetime.datetime) 
        for donation_datetime in db.query(DonationDatetime).filter(DonationDatetime.place_id == donation_place_id).all()
        ]

def db_add_user(db: Session, user_create: UserCreate) -> User:
    data = user_create.model_dump()
    db_existing_user = db.query(User).filter(User.telegram_id == user_create.telegram_id).first()
    if db_existing_user:
        user_update = UserUpdate.model_construct(id=db_existing_user.id, **data)
        return db_update_user(db, user_update)
    else:
        db_user = db.add(User(**data))
        db.commit()
        db.refresh(db_user)
        return db_user

def db_update_user(db: Session, user_update: UserUpdate) -> User:
    data = user_update.model_dump()
    db_user = db.query(User).filter(User.telegram_id == user_update.telegram_id).first()
    if db_user:
        for key, value in data.items():
            setattr(db_user, key, value)
        db.commit()
    
    return db_user