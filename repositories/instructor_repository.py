from db.run_sql import run_sql
from models.instructor import Instructor
from models.gym_class import GymClass
import repositories.location_repository as location_repository

def save(instructor):
    sql = "INSERT INTO instructors (full_name) VALUES (%s) RETURNING id"
    values = [instructor.name]

    result = run_sql(sql, values)
    instructor.id = result[0]["id"]

def select_all():
    instructors = []
    sql = "SELECT * FROM instructors"
    results = run_sql(sql)
    
    for row in results:
        instructor = Instructor(row["full_name"], row["id"])
        instructors.append(instructor)
    return instructors

def select(id):
    sql = "SELECT * FROM instructors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result is not None:
        instructor_found = Instructor(result[0]["full_name"], result[0]["id"])

    return instructor_found

def delete_all():
    sql = "DELETE FROM instructors"
    run_sql(sql)

def classes(instructor):
    classes_found = []

    sql = "SELECT * FROM gym_classes WHERE instructor_id = %s"
    values = [instructor.id]

    results = run_sql(sql, values)
    for row in results:
        location = location_repository.select(row["location_id"])
        class_found = GymClass(row["class_type"], 
            instructor, 
            row["class_date"], 
            row["class_time"], 
            row["duration"], 
            location, 
            row["id"]
        )
        classes_found.append(class_found)

    return classes_found