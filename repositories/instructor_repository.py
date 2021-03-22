from db.run_sql import run_sql
from models.instructor import Instructor

def save(instructor):
    sql = "INSERT INTO instructors (full_name) VALUES (%s) RETURNING id"
    values = [instructor.name]

    run_sql(sql, values)

def select_all():
    instructors = []
    sql = "SELECT * FROM instructors"
    results = run_sql(sql)
    
    for row in results:
        instructor = Instructor(row["full_name"])
        instructors.append(instructor)
    return instructors

def select(id):
    sql = "SELECT * FROM instructors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        instructor_found = Instructor(result["full_name"])

    return instructor_found