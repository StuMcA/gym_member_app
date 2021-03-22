from db.run_sql import run_sql
from models.gym_class import GymClass

def save(gym_class):
    sql = """
        INSERT INTO gym_classes
        (class_type, class_date, class_time, instructor, duration, class_location, capacity) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """
    values = [gym_class.class_type, gym_class.date, gym_class.time, gym_class.instructor, gym_class.duration, gym_class.location, gym_class.capacity]
    result = run_sql(sql, values)

    gym_class.id = result[0]['id']
                          

def select_all():
    all_classes = []
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    
    for row in results:
        gym_class = GymClass(row["class_type"], row["class_date"], row["class_time"], row["instructor"], row["duration"], row["class_locatin"], row["capacity"], row["id"])
        all_classes.append(gym_class)
    
    return all_classes

def select(id):
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        class_found = GymClass(result["class_type"], result["class_date"], result["class_time"], result["instructor"], result["duration"], result["class_locatin"], result["capacity"], result["id"])

    return class_found