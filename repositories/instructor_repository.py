from db.run_sql import run_sql
from models.instructor import Instructor

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