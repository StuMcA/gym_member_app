from flask import Flask, redirect, request, render_template, Blueprint
from datetime import time
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.attendance_repository as attendance_repository
from models.gym_class import GymClass
from models.member import Member

instructor_blueprint = Blueprint('instructor', __name__)