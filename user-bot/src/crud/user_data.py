
from sqlalchemy.orm import Session
from common.models import DonationDatetime, Faculty, DonationPlace

from schemas import DonationDatetimesDbResponse, DonationPlaceDbResponse

from functools import lru_cache

@lru_cache
def db_get_faculties_names(db: Session):
    return [faculty.name for faculty in db.query(Faculty).all()]

@lru_cache
def db_get_donation_places(db: Session) -> list[DonationPlaceDbResponse]:
    return [DonationPlaceDbResponse(id=donation_place.id, name=donation_place.name) for donation_place in db.query(DonationPlace).all()]

@lru_cache
def db_get_donation_datetimes(db: Session, donation_place_id: int) -> list[DonationDatetimesDbResponse]:
    return [
        DonationDatetimesDbResponse(id=donation_datetime.id, place_id = donation_datetime.place_id,datetime=donation_datetime.datetime) 
        for donation_datetime in db.query(DonationDatetime).filter(DonationDatetime.place_id == donation_place_id).all()
        ]