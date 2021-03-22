from db.run_sql import run_sql
from models.location import Location

def save(location):
    sql = "INSERT INTO locations (room_name, capacity) VALUES (%s, %s)"
    values = [location.room_name, location.capacity]

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