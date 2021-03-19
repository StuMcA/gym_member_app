import repositories.member_repository as member_repository
from models.member import Member

member_1 = Member("Stuart", "McAra", 32, "Peak")
member_2 = Member("Michael", "Scott", 45, "Off-peak")

member_repository.save(member_1)
member_repository.save(member_2)