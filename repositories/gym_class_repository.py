from db.run_sql import run_sql
from models.gym_class import Class

def save(gym_class):
    sql = """
        INSERT INTO gym_classes
        
    """
    gym_class = Gym_class(gym_class.class_type, 
                          gym_class.instructor, 
                          gym_class.date, 
                          gym_class.time, 
                          gym_class.duration, 
                          gym_class.location, 
                          gym_class.capacity
                          )
