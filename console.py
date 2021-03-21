import repositories.member_repository as member_repository
from models.member import Member

member_repository.delete_all()

member_1 = Member("Stuart", "McAra", '1989-03-26', "Peak")
member_2 = Member("Michael", "Scott", '1965-12-03', "Off-peak")

member_repository.save(member_1)
member_repository.save(member_2)