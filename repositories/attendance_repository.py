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
        gym_class = gym_class_repository.select(result[0]["class_id"])
        member = member_repository.select(result[0]["member_id"])
        attendance = Attendance(gym_class, member, id)

    return attendance

def select_by_class_and_member(gym_class, member):
    attendees = []
    sql = "SELECT * FROM attendees WHERE class_id = %s AND member_id = %s"
    values = [gym_class.id, member.id]
    results = run_sql(sql, values)

    for result in results:
        gym_class = gym_class_repository.select(result["class_id"])
        member = member_repository.select(result["member_id"])
        attendance = Attendance(gym_class, member, result["id"])
        attendees.append(attendance)

    return attendees

def select_by_member(member):
    attendees = []
    sql = "SELECT * FROM attendees WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for result in results:
        gym_class = gym_class_repository.select(result["class_id"])
        member = member_repository.select(result["member_id"])
        attendance = Attendance(gym_class, member, result["id"])
        attendees.append(attendance)

    return attendees

def select_by_class(gym_class):
    attendees = []
    sql = "SELECT * FROM attendees WHERE class_id = %s"
    values = [gym_class.id]
    results = run_sql(sql, values)

    for result in results:
        gym_class = gym_class_repository.select(result["class_id"])
        member = member_repository.select(result["member_id"])
        attendance = Attendance(gym_class, member, result["id"])
        attendees.append(attendance)

    return attendees


def delete_all():
    sql = "DELETE FROM attendees"
    run_sql(sql)

def delete_by_class_id(id):
    sql = "DELETE FROM attendees WHERE class_id = %s"
    values = [id]
    run_sql(sql, values)

def delete_by_member_id(id):
    sql = "DELETE FROM attendees WHERE member_id = %s"
    values = [id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM attendees WHERE id = %s"
    values = [id]
    run_sql(sql, values)