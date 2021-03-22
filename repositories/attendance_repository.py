from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member
from models.attendance import Attendance
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

def save(attendance):
    sql = """
        INSERT INTO attendees (class_id, member_id)
        VALUES (%s, %s)
        RETURNING id
    """
    values = [attendance.gym_class.id, attendance.member.id]
    result = run_sql(sql, values)
    attendance.id = result[0]["id"]

def select_all():
    all_attendances = []
    sql = "SELECT * FROM attendees"
    results = run_sql(sql)

    for result in results:
        gym_class = gym_class_repository.select(result["class_id"])
        member = member_repository.select(result["member_id"])
        attendance = Attendance(gym_class, member, id)
        all_attendances.append(attendance)

    return all_attendances

def select(id):
    sql = "SELECT * FROM attendees WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    
    if result is not None:
        gym_class = gym_class_repository.select(result["class_id"])
        member = member_repository.select(result["member_id"])
        attendance = Attendance(gym_class, member, id)

    return attendance

def delete_all():
    sql = "DELETE FROM attendees"
    run_sql(sql)