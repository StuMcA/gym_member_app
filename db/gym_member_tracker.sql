DROP TABLE IF EXISTS attendees;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS classes;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_of_birth DATE,
    membership VARCHAR(255)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    class_type VARCHAR(255),
    class_date VARCHAR(255),
    class_time VARCHAR(255)
);

CREATE TABLE attendees (
    id SERIAL PRIMARY KEY,
    class_id INT REFERENCES classes(id),
    member_id INT REFERENCES members(id)
);