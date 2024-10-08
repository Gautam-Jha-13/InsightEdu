import xml.etree.ElementTree as ET
from xml.dom import minidom
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define the XML file name
xml_file = "StudentInfo3T.xml"

# Define the streams
streams = ['Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Chemical Engineering']

# Create the root element
root = ET.Element("root")  # Main root element

# Generate fake data
for student_id in range(360, 410):  # Generate 50 records (360 to 409 inclusive)
    row = ET.SubElement(root, "row")  # Each student data is wrapped in a <row> tag
    
    ET.SubElement(row, "student_id").text = str(student_id)
    ET.SubElement(row, "name").text = fake.name()
    ET.SubElement(row, "age").text = str(random.randint(18, 25))
    ET.SubElement(row, "gender").text = random.choice(['male', 'female', 'other'])
    ET.SubElement(row, "stream").text = random.choice(streams)
    ET.SubElement(row, "internships").text = str(random.randint(0, 3))
    ET.SubElement(row, "history_of_backlogs").text = str(random.randint(0, 5))
    placed_or_not_value = 1 if random.choice([True, False]) else 0
    ET.SubElement(row, "placed_or_not").text = str(placed_or_not_value)  # Use '1' for True and '0' for False
    ET.SubElement(row, "created_at").text = fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')

# Create a pretty-printed XML string
xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")

# Write the XML string to the file
with open(xml_file, "w", encoding="utf-8") as f:
    f.write(xml_str)

print(f"50 fake student records have been generated and saved to {xml_file}")
