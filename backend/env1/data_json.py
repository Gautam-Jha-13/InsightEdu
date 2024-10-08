import json
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define the JSON file name
json_file = "StudentInfo3T.json"

# Define the streams
streams = ['Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Chemical Engineering']

# Generate fake data
students = []
for student_id in range(220, 321):  # Generate 101 records (220 to 320 inclusive)
    name = fake.name()
    age = random.randint(18, 25)
    gender = random.choice(['male', 'female', 'other'])
    stream = random.choice(streams)
    internships = random.randint(0, 3)
    history_of_backlogs = random.randint(0, 5)
    placed_or_not = random.choice([True, False])
    created_at = fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
    
    # Generate random grades
    grades = [random.randint(60, 100) for _ in range(3)]

    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "gender": gender,
        "stream": stream,
        "internships": internships,
        "history_of_backlogs": history_of_backlogs,
        "placed_or_not": placed_or_not,
        "created_at": created_at,
    }
    
    students.append(student)

# Write the data to the JSON file
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(students, f, indent=2)

print(f"101 fake student records have been generated and saved to {json_file}")