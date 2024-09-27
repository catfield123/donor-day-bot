from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Boolean, Enum, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from enum import Enum as PyEnum

Base = declarative_base()

class FoundingSourceEnum(PyEnum):
    budget = 'budget'
    contract = 'contract'

class SexEnum(PyEnum):
    male = 'male'
    female = 'female'

class BodyWeightEnum(PyEnum):
    more_then_58_kg = 'Больше 58 кг.'
    between_50_and_58_kg = 'От 50 до 58 кг.'
    less_then_50_kg = 'Меньше 50 кг.'

class DonorStatusEnum(PyEnum):
    confirmed = 'confirmed'
    unconfirmed = 'unconfirmed'
    not_specified = 'not specified'

class Faculty(Base):
    __tablename__ = 'faculty'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable = False)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True, nullable=False)

    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)

    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    patronymic = Column(String, nullable=True)

    is_polytech_student = Column(Boolean, nullable=False)
    grade_book_number = Column(String, nullable=True)
    group_number = Column(String, nullable=True)
    faculty_id = Column(Integer, ForeignKey('faculty.id'), nullable=True)
    faculty = relationship("Faculty")
    founding_source = Column(Enum(FoundingSourceEnum), name='founding_source', nullable=True)

    inn = Column(String, nullable=False)
    snils = Column(String, nullable=False)

    passport_series = Column(String, nullable=False)
    passport_number = Column(String, nullable=False)
    passport_issued_by = Column(String, nullable=False)
    passport_issued_date = Column(Date, nullable=False)
    passport_issued_organization_code = Column(String, nullable=False)

    birth_date = Column(Date, nullable=False)
    birth_place = Column(String, nullable=False)
    registration_address = Column(String, nullable=False)

    sex = Column(Enum(SexEnum), name='sex', nullable=False)
    body_weight = Column(Enum(BodyWeightEnum), name='body_weight', nullable=False)

    bone_marrow_typing_agreement = Column(Boolean, nullable=False)

    donation_place = Column(String, nullable=False)
    donation_datetime = Column(TIMESTAMP, nullable=False)

    donor_status = Column(Enum(DonorStatusEnum), nullable=False, name='donor_status', default='not specified')

    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')


class Admin(Base):
    __tablename__ = 'admin'
    telegram_id = Column(String, primary_key=True)


class Volunteer(Base):
    __tablename__ = 'volunteer'
    telegram_id = Column(String, primary_key=True)
    granted_by_telegram_id = Column(String, ForeignKey('admin.telegram_id'), nullable=False)