DROP TABLE IF EXISTS attendees;
DROP TABLE IF EXISTS gym_classes;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS locations;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_of_birth DATE,
    membership VARCHAR(255)
);

CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255)
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    room_name VARCHAR(255),
    capacity INT
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    class_type VARCHAR(255),
    class_date VARCHAR(255),
    class_time TIME,
    instructor_id INT REFERENCES instructors(id),
    duration INT,
    location_id INT REFERENCES locations(id)
);

CREATE TABLE attendees (
    id SERIAL PRIMARY KEY,
    class_id INT REFERENCES gym_classes(id),
    member_id INT REFERENCES members(id)
);