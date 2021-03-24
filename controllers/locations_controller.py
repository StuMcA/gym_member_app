from flask import Flask, redirect, request, render_template, Blueprint
import repositories.location_repository as location_repository
from models.gym_class import GymClass
from models.location import Location

location_blueprint = Blueprint('location', __name__)

@location_blueprint.route('/locations')
def index():
    all_locations = location_repository.select_all()
    return render_template('locations/index.html', title="locations", locations=all_locations)

@location_blueprint.route('/locations/<id>')
def location(id):
    location = location_repository.select(id)
    classes_found = location_repository.classes(location)
    return render_template('/locations/show.html', location=location, classes=classes_found)

@location_blueprint.route('/locations/<id>/edit')
def edit_location(id):
    location_found = location_repository.select(id)
    return render_template('/locations/edit.html', location=location_found)

@location_blueprint.route('/locations/<id>', methods=['POST'])
def update_location(id):
    location = Location(request.form["new_name"], id)
    location_repository.update(location)
    return redirect(f'/locations/{id}')

@location_blueprint.route('/locations/<id>/delete', methods=['POST'])
def destroy_location(id):
    location_repository.delete(id)
    return redirect('/locations')