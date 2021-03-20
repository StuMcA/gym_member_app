from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = """
        INSERT INTO members (first_name, last_name, date_of_birth, membership)
        VALUES (%s, %s, %s, %s) RETURNING id
    """
    values = [member.first_name, member.last_name, member.date_of_birth, member.membership]
    result = run_sql(sql, values)

    member.id = result[0]['id']

def select_all():
    all_members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['date_of_birth'], row['membership'])
        all_members.append(member)

    return all_members

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]

    result = run_sql(sql, values)[0]
    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['date_of_birth'], result['membership'], result['id'])
    return member