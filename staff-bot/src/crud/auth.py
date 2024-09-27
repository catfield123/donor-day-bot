from sqlalchemy.orm import Session
from common.models import Admin, Volunteer

from schemas import CheckAuthRequestSchema

def db_is_admin(db: Session, check_auth_request: CheckAuthRequestSchema) -> bool:
    return bool(db.query(Admin).filter(Admin.telegram_id == check_auth_request.telegram_id).first())

def db_is_volunteer(db: Session, check_auth_request: CheckAuthRequestSchema) -> bool:
    return bool(db.query(Volunteer).filter(Volunteer.telegram_id == check_auth_request.telegram_id).first())

def db_is_admin_or_volunteer(db: Session, check_auth_request: CheckAuthRequestSchema) -> bool:
    return db_is_admin(db, check_auth_request.telegram_id) or db_is_volunteer(db, check_auth_request.telegram_id)

