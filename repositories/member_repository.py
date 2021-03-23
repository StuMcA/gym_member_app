from db.run_sql import run_sql
from models.member import Member
from models.gym_class import GymClass
import repositories.attendance_repository as attendance_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository


# CRUD operations
def save(member):
    sql = """
        INSERT INTO members (first_name, last_name, date_of_birth, membership)
        VALUES (%s, %s, %s, %s) RETURNING id
    """
    values = [member.first_name, member.last_name, member.date_of_birth, member.membership]
    result = run_sql(sql, values)

    member.id = result[0]['id']

def select_all():
    all_members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['date_of_birth'], row['membership'], row['id'])
        all_members.append(member)

    return all_members

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]

    result = run_sql(sql, values)[0]
    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['date_of_birth'], result['membership'], result['id'])
    return member

def update(member):
    sql = """
        UPDATE members
        SET (first_name, last_name, date_of_birth, membership) = (%s, %s, %s, %s)
        WHERE id = %s
    """
    values = (member.first_name, member.last_name, member.date_of_birth, member.membership, member.id)
    run_sql(sql, values)

def delete(id):
    attendance_repository.delete_by_member_id(id)
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

# Gym class interactions
def classes(member):
    gym_classes = []

    sql = "SELECT gym_classes.* FROM gym_classes INNER JOIN attendees ON attendees.class_id = gym_classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

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
        gym_classes.append(gym_class)
    
    return gym_classes