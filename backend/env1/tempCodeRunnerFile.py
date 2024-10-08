import csv
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define the CSV file name
csv_file = "StudentInfo3fake.xml"

# Define the header for the CSV file
header = ['student_id', 'name', 'age', 'gender', 'stream', 'internships', 'history_of_backlogs', 'placed_or_not', 'created_at']

# Define the streams
streams = ['Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Chemical Engineering']

# Open the CSV file and write the data
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(header)
    
    # Generate and write fake data
    for student_id in range(102, 202):  # Generate 100 records
        name = fake.name()
        age = random.randint(18, 25)
        gender = random.choice(['male', 'female', 'other'])
        stream = random.choice(streams)
        
        internships = random.randint(0, 3)
        history_of_backlogs = random.randint(0, 5)
        placed_or_not = random.choice([True, False])
        created_at = fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')

        # Write the data to the CSV file
        writer.writerow([student_id, name, age, gender, stream, internships, history_of_backlogs, placed_or_not, created_at])

print(f"100 fake student records have been generated and saved to {csv_file}")