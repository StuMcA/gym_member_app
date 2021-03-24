from db.run_sql import run_sql
from models.location import Location
from models.gym_class import GymClass
import repositories.instructor_repository as instructor_repository

def save(location):
    sql = "INSERT INTO locations (room_name, capacity) VALUES (%s, %s) RETURNING id"
    values = [location.name, location.capacity]

    result = run_sql(sql, values)
    location.id = result[0]["id"]

def select_all():
    locations = []
    sql = "SELECT * FROM locations"
    results = run_sql(sql)

    for row in results:
        location = Location(row["room_name"], row["capacity"], row["id"])
        locations.append(location)

    return locations

def select(id):
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    # import pdb
    # pdb.set_trace()

    result = run_sql(sql, values)[0]

    if result is not None:
        location = Location(result["room_name"], result["capacity"], id)
    return location

def delete(id):
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)

def classes(location):
    classes_found = []

    sql = "SELECT * FROM gym_classes WHERE location_id = %s"
    values = [location.id]

    results = run_sql(sql, values)
    for row in results:
        instructor = instructor_repository.select(row["instructor_id"])
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