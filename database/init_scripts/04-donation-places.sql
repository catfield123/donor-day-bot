CREATE TABLE donation_place (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

INSERT INTO donation_place (name) VALUES
    ('Башня Политеха'),
    ('Елизаветинская больница')
;

CREATE TABLE donation_datetime (
    id SERIAL PRIMARY KEY,
    place_id INTEGER NOT NULL REFERENCES donation_place(id),
    datetime TIMESTAMP WITH TIME ZONE NOT NULL,
)