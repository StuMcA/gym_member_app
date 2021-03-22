from db.run_sql import run_sql
from models.gym_class import GymClass

def save(gym_class):
    sql = """
        INSERT INTO gym_classes
        (class_type, class_date, class_time, duration, class_location, capacity) 
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id
    """
    values = [gym_class.instructor, gym_class.date, gym_class.time, gym_class.duration, gym_class.location, gym_class.capacity]
    result = run_sql(sql, values)

    gym_class.id = result[0]['id']
                          
