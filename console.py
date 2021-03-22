import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.instructor_repository as instructor_repository
from models.member import Member
from models.gym_class import GymClass
from models.instructor import Instructor

member_repository.delete_all()

member_1 = Member("Stuart", "McAra", '1989-03-26', "Peak")
member_2 = Member("Michael", "Scott", '1965-12-03', "Off-peak")

member_repository.save(member_1)
member_repository.save(member_2)

instructor_1 = Instructor("Big Jane")
instructor_2 = Instructor("Bendy Jo")

instructor_repository.save(instructor_1)
instructor_repository.save(instructor_2)

class_1 = GymClass("Weights", instructor_1, "2021-03-23", "14:00", 90, "Weights Studio", 15)
class_2 = GymClass("Yoga", instructor_2, "2021-03-23", "13:30", 60, "Yoga Studio", 10)

gym_class_repository.save(class_1)
gym_class_repository.save(class_2)


