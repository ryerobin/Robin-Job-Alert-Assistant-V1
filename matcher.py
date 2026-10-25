## this code calculates the match percentage between a job's required skills and the user's skills
from jobs import jobs
my_skills = ["Python", "Power BI", "SQL"]


def calculate_match(job, location, my_skills):
    skill_matches = 0
    
    for skill in job["skills"]:
        if skill in my_skills:
            skill_matches += 1
            
    skill_score = skill_matches / len(job["skills"]) * 90

    location_score = 0
    if location == job["location"]:
        location_score = 10

    return skill_score + location_score