CREATE TABLE donation_place (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

INSERT INTO donation_place VALUES 
    ("Башня Политеха"),
    ("Елизаветинская больница")
;

CREATE TABLE donation_datetime (
    place_id INTEGER NOT NULL REFERENCES donation_place(id),
    datetime TIMESTAMP NOT NULL,

    PRIMARY KEY (place_id, datetime)
)