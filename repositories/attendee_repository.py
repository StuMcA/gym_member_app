from db.run_sql import run_sql

def select_all():
    sql = "SELECT * FROM attendees"
    results = run_sql(sql)
    return results
