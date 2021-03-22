import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.instructor_repository as instructor_repository
import repositories.attendance_repository as attendance_repository
from models.member import Member
from models.gym_class import GymClass
from models.instructor import Instructor
from models.attendance import Attendance
from models.location import Location

member_repository.delete_all()
gym_class_repository.delete_all()
attendance_repository.delete_all()

member_1 = Member("Stuart", "McAra", '1989-03-26', "Peak")
member_2 = Member("Michael", "Scott", '1965-12-03', "Off-peak")

member_repository.save(member_1)
member_repository.save(member_2)

instructor_1 = Instructor("Big Jane")
instructor_2 = Instructor("Bendy Jo")

instructor_repository.save(instructor_1)
instructor_repository.save(instructor_2)

location_1 = Location("Weights Studio", 15)
location_2 = Location("Yoga Studio", 10)

class_1 = GymClass("Weights", instructor_1, "2021-03-23", "14:00", 90, location_1)
class_2 = GymClass("Yoga", instructor_2, "2021-03-23", "13:30", 60, location_2)

gym_class_repository.save(class_1)
gym_class_repository.save(class_2)

attendance_1 = Attendance(class_1, member_1)
attendance_2 = Attendance(class_1, member_2)
attendance_3 = Attendance(class_2, member_1)

attendance_repository.save(attendance_1)
attendance_repository.save(attendance_2)
attendance_repository.save(attendance_3)

