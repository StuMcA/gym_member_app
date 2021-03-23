from flask import Flask, redirect, request, render_template, Blueprint
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.attendance_repository as attendance_repository
from models.gym_class import GymClass
from models.member import Member
from models.attendance import Attendance

attendance_blueprint = Blueprint('attendance', __name__)


@attendance_blueprint.route('/attendances/new', methods=["POST"])
def create():
    gym_class = gym_class_repository.select(request.form["class_id"])
    member = member_repository.select(request.form["member_id"])
    existing_attendances = attendance_repository.select_by_class_and_member(gym_class, member)
    if len(existing_attendances) > 0:
        return redirect(f'/classes/{gym_class.id}')
    else:
        attendance = Attendance(gym_class, member)
        attendance_repository.save(attendance)

        return redirect(f'/classes/{gym_class.id}')

@attendance_blueprint.route('/attendances/<id>/delete', methods=["POST"])
def destroy(id):
    return_to = request.form['return_to']

    attendance = attendance_repository.select(id)
    
    gym_class_id = attendance.gym_class.id
    member_id = attendance.member.id

    attendance_repository.delete(id)

    if return_to == "classes":
        return redirect(f'/classes/{gym_class_id}')
    else:
        return redirect(f'/members/{member_id}')