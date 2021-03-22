import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
from models.member import Member
from models.gym_class import GymClass

member_repository.delete_all()

member_1 = Member("Stuart", "McAra", '1989-03-26', "Peak")
member_2 = Member("Michael", "Scott", '1965-12-03', "Off-peak")

member_repository.save(member_1)
member_repository.save(member_2)

class_1 = GymClass("Weights", "Big Jane", "2021-03-23", "14:00", 90, "Weights Studio", 15)
class_2 = GymClass("Yoga", "Bendy Jo", "2021-03-23", "13:30", 60, "Yoga Studio", 10)

gym_class_repository.save(class_1)
gym_class_repository.save(class_2)


