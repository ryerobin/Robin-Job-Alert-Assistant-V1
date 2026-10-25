## Linkedin Job Alert Assistant V1
## This script automates the process of checking for new job postings on LinkedIn based on specified criteria. It will look for specific job titles, skills, and locations and send a notification to my phone
from jobs import jobs
from matcher import calculate_match

skills_input = input("Enter 3 skills separated by commas:")
my_skills = [
    skill.strip()
    for skill in skills_input.split(",")      
]

my_salary_expectations = int(input("Enter your minimum salary expectations: "))

location_input = input("Enter your preferred location: ")
location = [
    location_input.strip()
    for location in location_input.split(";")
]
matches = []

for job in jobs:
    if(skill in my_skills for skill in job["skills"]):
        if job["salary"] >= my_salary_expectations:
            percentage = calculate_match(job, location, my_skills)
            if percentage > 0:
                matches.append((percentage, job))
                

matches.sort(key=lambda x: x[0], reverse=True,)

for percentage, job in matches:
    print()
    print(f"We matched you with a job: {job['title']} matches with skills {job['skills']}.")
    print(f"The salary is ${job['salary']}")
    print(f"Location: {job['location']}")
    print(f"Match Percentage: {percentage}%")
