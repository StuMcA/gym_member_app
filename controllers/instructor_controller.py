from flask import Flask, redirect, request, render_template, Blueprint
import repositories.instructor_repository as instructor_repository
from models.instructor import Instructor

instructor_blueprint = Blueprint('instructor', __name__)

@instructor_blueprint.route('/instructors')
def index():
    all_instructors = instructor_repository.select_all()
    return render_template('instructors/index.html', title="Instructors", instructors=all_instructors)

@instructor_blueprint.route('/instructors/<id>')
def instructor(id):
    instructor = instructor_repository.select(id)
    classes_sorted = sorted(instructor_repository.classes(instructor), key = lambda instructor: (instructor.date, instructor.time))
    return render_template('/instructors/show.html', instructor=instructor, classes=classes_sorted)

@instructor_blueprint.route('/instructors/new')
def new_instructor():
    return render_template('/instructors/new.html', title="Add new instructor")


@instructor_blueprint.route('/instructors/create', methods=['POST'])
def create_instructor():
    instructor = Instructor(
        request.form['full_name']
    )
    instructor_repository.save(instructor)
    return redirect('/instructors')

@instructor_blueprint.route('/instructors/<id>/edit')
def edit_instructor(id):
    instructor_found = instructor_repository.select(id)
    return render_template('/instructors/edit.html', instructor=instructor_found)

@instructor_blueprint.route('/instructors/<id>', methods=['POST'])
def update_instructor(id):
    instructor = Instructor(request.form["new_name"], id)
    instructor_repository.update(instructor)
    return redirect(f'/instructors/{id}')

@instructor_blueprint.route('/instructors/<id>/delete', methods=['POST'])
def destroy_instructor(id):
    instructor_repository.delete(id)
    return redirect('/instructors')