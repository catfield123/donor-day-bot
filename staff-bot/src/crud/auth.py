from sqlalchemy.orm import Session
from common.models import Admin, Volunteer

def is_admin(db: Session, telegram_id: str) -> bool:
    return bool(db.query(Admin).filter(Admin.telegram_id == telegram_id).first())

def is_volunteer(db: Session, telegram_id: str) -> bool:
    return bool(db.query(Volunteer).filter(Volunteer.telegram_id == telegram_id).first())

def is_admin_or_volunteer(db: Session, telegram_id: str) -> bool:
    return is_admin(db, telegram_id) or is_volunteer(db, telegram_id)

