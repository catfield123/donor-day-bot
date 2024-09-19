CREATE TYPE faculty AS ENUM (
    'ГИ',
    'ИСИ',
    'ИБСИБ',
    'ИКНК',
    'ИММИТ',
    'ИФИМ',
    'ИФКСТ',
    'ИЭИТ',
    'ИЭ',
    'ПИШ Цифровой инжиниринг',  
    'ФизМех',
    'ИПМЭИТ'
);

CREATE TYPE founding_source as ENUM (
    'budget',
    'contract'
);

CREATE TYPE sex as ENUM (
    'male',
    'female'
);

CREATE TYPE body_weight as ENUM (
    'Больше 58 кг.',
    'От 50 до 58 кг.',
    'Меньше 50 кг.'
);

CREATE TYPE "donor_status" as ENUM (
    "confirmed",
    "unconfirmed",
    "not specified"
);

CREATE TABLE "user" (
    id INTEGER PRIMARY KEY,

    telegram_id TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email TEXT NOT NULL,

    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    patronymic TEXT,


    is_polytech_student BOOL NOT NULL,
    grade_book_number CHAR(8),
    group_number TEXT,
    faculty faculty,
    founding_source founding_source,

    inn TEXT NOT NULL,
    snils TEXT NOT NULL,

    passport_series CHAR(4) NOT NULL,
    passport_number CHAR(6) NOT NULL,
    passport_issued_by TEXT NOT NULL,
    passport_issued_date DATE NOT NULL,
    passport_issued_organization_code TEXT NOT NULL,

    birth_date DATE NOT NULL,
    birth_place TEXT NOT NULL,
    registration_address TEXT NOT NULL,

    sex sex NOT NULL,
    body_weight body_weight NOT NULL,

    bone_marrow_typing_agreement BOOL NOT NULL,

    donation_place TEXT NOT NULL,
    donation TIMESTAMP WITH TIME ZONE NOT NULL,

    donor_status donor_status NOT NULL DEFAULT 'not specified',
    
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER autoupdate_user
BEFORE INSERT OR UPDATE ON "user"
FOR EACH ROW
EXECUTE FUNCTION refresh_last_updated();


CREATE INDEX ON "user" (name);
ANALYZE "user";



CREATE TABLE user_pd_agreement (
    telegram_id TEXT PRIMARY KEY,
    pd_agreement BOOL NOT NULL DEFAULT FALSE
);