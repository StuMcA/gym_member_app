from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository
import repositories.attendance_repository as attendance_repository

# CRUD operations

def save(gym_class):
    sql = """
        INSERT INTO gym_classes
        (class_type, class_date, class_time, instructor_id, duration, location_id) 
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id;
    """
    values = [gym_class.class_type, gym_class.date, gym_class.time, gym_class.instructor.id, gym_class.duration, gym_class.location.id]
    result = run_sql(sql, values)

    gym_class.id = result[0]['id']
                          

def select_all():
    all_classes = []
    sql = "SELECT * FROM gym_classes ORDER BY class_date, class_time"
    results = run_sql(sql)
    
    for row in results:
        instructor = instructor_repository.select(row["instructor_id"])
        location = location_repository.select(row["location_id"])
        gym_class = GymClass(row["class_type"], 
            instructor, 
            row["class_date"], 
            row["class_time"], 
            row["duration"], 
            location, 
            row["id"]
        )
        all_classes.append(gym_class)
    
    return all_classes

def select(id):
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        instructor = instructor_repository.select(result["instructor_id"])
        location = location_repository.select(result["location_id"])
        class_found = GymClass(result["class_type"], 
        instructor, 
        result["class_date"], 
        result["class_time"], 
        result["duration"], 
        location, 
        result["id"]
    )

    return class_found

def update(gym_class):
    sql = """
        UPDATE gym_classes
        SET (class_type, class_date, class_time, instructor_id, duration, location_id) = (%s, %s, %s, %s, %s, %s)
        WHERE id = %s
    
    """
    values = [gym_class.class_type, gym_class.date, gym_class.time, gym_class.instructor.id, gym_class.duration, gym_class.location.id, gym_class.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

def delete(id):
    attendance_repository.delete_by_class_id(id)
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Member interactions

def add_member(gym_class, member):
    sql = "INSERT INTO attendees (class_id, member_id) VALUES (%s, %s)"
    values = [gym_class.id, member.id]
    run_sql(sql, values)
    

def members(gym_class):
    attendees = []
    sql = "SELECT members.* FROM members INNER JOIN attendees ON attendees.member_id = members.id WHERE class_id = %s"
    values = [gym_class.id]
    results = run_sql(sql, values)

    for row in results:
        attendee = Member(row["first_name"], row["last_name"], row["date_of_birth"], row["membership"], row["id"])
        attendees.append(attendee)

    return attendees