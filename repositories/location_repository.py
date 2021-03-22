from db.run_sql import run_sql
from models.location import Location

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