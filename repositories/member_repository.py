from db.run_sql import run_sql
from models.member import Members

def save(member):
    sql = """
        INSERT INTO members (first_name, last_name, age, membership)
        VALUES (%s, %s, %s, %s) RETURNING id
    """
    values = [member.first_name, member.last_name, member.age, member.membership]
    result = run_sql(sql, values)

    member.id = results[0]['id']

def select_all():
    all_members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['age'], row['membership'])
        all_members.append(member)

    return all_members