import pymysql
# Database configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'hustle_db'
}

db_config2 = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'hustle_db'
}

def get_locations():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT location_name FROM locations")
    locations = cursor.fetchall()
    cursor.close()
    connection.close()
    return locations

def get_jobType():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT id, jobtype_name FROM jobtypes")
    type = cursor.fetchall()
    cursor.close()
    connection.close()
    return type

def get_salaryRange():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT id, salary_range FROM salaryranges")
    range = cursor.fetchall()
    cursor.close()
    connection.close()
    return range

# def get_featured_jobs():
#     connection = pymysql.connect(**db_config)
#     cursor = connection.cursor()
#     cursor.execute("SELECT companies.company_name, companies.company_logo, postedjobs.job_title, jobtypes.jobtype_name, locations.location_name, GROUP_CONCAT( skills.skill_name SEPARATOR',') as skills FROM postedjobs LEFT JOIN companies ON postedjobs.company_id = companies.id left JOIN locations ON locations.id = postedjobs.job_location_id LEFT JOIN jobtypes ON jobtypes.id = postedjobs.jobtype_id LEFT JOIN postedjobs_skills ON postedjobs.id = postedjobs_skills.posted_job_id LEFT JOIN skills ON skills.id = postedjobs_skills.skill_id GROUP BY companies.company_name, companies.company_logo, postedjobs.job_title, jobtypes.jobtype_name, locations.location_name")
#     featured_jobs = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return featured_jobs


def get_featured_jobs(job_title=None, location=None, job_type=None, salary_range=None):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    query = """
    SELECT companies.company_name, companies.company_logo, postedjobs.job_title,
      CASE 
        WHEN TIMESTAMPDIFF(MINUTE, postedjobs.updated_at, NOW()) < 60 THEN CONCAT(TIMESTAMPDIFF(MINUTE, postedjobs.updated_at, NOW()), ' Min Ago')
        WHEN TIMESTAMPDIFF(HOUR, postedjobs.updated_at, NOW()) < 24 THEN CONCAT(TIMESTAMPDIFF(HOUR, postedjobs.updated_at, NOW()), ' Hrs Ago')
        WHEN DATEDIFF(NOW(), postedjobs.updated_at) < 7 THEN CONCAT(DATEDIFF(NOW(), postedjobs.updated_at), ' Days Ago')
        WHEN DATEDIFF(NOW(), postedjobs.updated_at) < 30 THEN CONCAT(FLOOR(DATEDIFF(NOW(), postedjobs.updated_at) / 7), ' Weeks Ago')
        WHEN DATEDIFF(NOW(), postedjobs.updated_at) < 365 THEN CONCAT(FLOOR(DATEDIFF(NOW(), postedjobs.updated_at) / 30), ' Months Ago')
        ELSE CONCAT(FLOOR(DATEDIFF(NOW(), postedjobs.updated_at) / 365), ' Years Ago')
    END AS time_ago, jobtypes.jobtype_name, locations.location_name,
    GROUP_CONCAT(skills.skill_name SEPARATOR ',') as skills
    FROM postedjobs
    LEFT JOIN companies ON postedjobs.company_id = companies.id
    LEFT JOIN locations ON locations.id = postedjobs.job_location_id
    LEFT JOIN jobtypes ON jobtypes.id = postedjobs.jobtype_id
    LEFT JOIN postedjobs_skills ON postedjobs.id = postedjobs_skills.posted_job_id
    LEFT JOIN skills ON skills.id = postedjobs_skills.skill_id
    WHERE 1=1
    """

    params = []
    if job_title:
        query += " AND postedjobs.job_title LIKE %s"
        params.append(f"%{job_title}%")
    if location:
        query += " AND locations.location_name = %s"
        params.append(location)
    if job_type:
        query += " AND jobtypes.id = %s"
        params.append(job_type)
    if salary_range:
        query += " AND postedjobs.salary_range_id = %s"
        params.append(salary_range)

    query += " GROUP BY companies.company_name, companies.company_logo, postedjobs.job_title, jobtypes.jobtype_name, locations.location_name"

    cursor.execute(query, params)
    featured_jobs = cursor.fetchall()

    cursor.close()
    connection.close()
    return featured_jobs


def get_companies(page=1, per_page=5):
    offset = (page - 1) * per_page
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM companies")
    total_records = cursor.fetchone()[0]
    cursor.execute("SELECT * FROM companies LIMIT %s OFFSET %s", (per_page, offset))
    companies = cursor.fetchall()
    cursor.close()
    connection.close()
    return companies, total_records


def get_jobs():
    sql = '''
    SELECT companies.company_name, companies.company_email, postedjobs.job_title, jobtypes.jobtype_name, locations.location_name FROM ( (postedjobs INNER JOIN companies ON postedjobs.company_id = companies.id) INNER JOIN locations ON companies.id = locations.id) INNER JOIN jobtypes ON companies.id = jobtypes.id
       '''

def get_talents(job_title=None,location=None):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    sql = """select * from  candidates
    where 1=1 """
    params = []
    if job_title:
        sql += " AND professional_title LIKE %s"
        params.append(f"%{job_title}%")
    if location:
        sql += " AND address = %s"
        params.append(location)
    cursor.execute(sql, params)
    devs = cursor.fetchall()
    cursor.close()
    connection.close()
    return devs

def candidates_locations():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT address FROM candidates ")
    locations = cursor.fetchall()
    cursor.close()
    connection.close()
    return locations

def developer_tags():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT professional_title FROM candidates limit 10")
    tags = cursor.fetchall()
    cursor.close()
    connection.close()
    return tags

from datetime import datetime, timedelta
import pytz

def time_ago(date):
    if date is None:
        return 'recently'
    
    now = datetime.now(pytz.utc)
    diff = now - date

    if diff.days >= 365:
        years = diff.days // 365
        return f'{years} Yr' if years > 1 else '1 Yr'
    elif diff.days >= 30:
        months = diff.days // 30
        return f'{months} M' if months > 1 else '1 M'
    elif diff.days > 0:
        return f'{diff.days} Day' if diff.days > 1 else '1 Day'
    elif diff.seconds >= 3600:
        hours = diff.seconds // 3600
        return f'{hours} Hr' if hours > 1 else '1 Hr'
    elif diff.seconds >= 60:
        minutes = diff.seconds // 60
        return f'{minutes} Min' if minutes > 1 else '1 Min'
    else:
        return 'Now'
    


def get_candidates():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM candidates")
    candidates = cursor.fetchall()
    cursor.close()
    connection.close()
    return candidates