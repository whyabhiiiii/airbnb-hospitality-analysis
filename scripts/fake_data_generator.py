# Install Faker library if not installed
# !pip install faker

from faker import Faker
import random
import pandas as pd

# Initialize Faker object
fake = Faker()

# List of numbers as per your image
rows = [13, 83, 9, 171, 8, 5, 250, 175, 40, 69, 240, 36, 
        110, 256, 2, 241, 142, 115, 314, 243, 147, 71, 
        1, 10, 89, 7, 15, 28, 12, 20, 3, 6, 4, 14, 74, 11]

# Function to generate random image URLs for men and women
def generate_image_url():
    gender = random.choice(['men', 'women'])
    img_id = random.randint(1, 99)  # Random ID between 1 and 99
    return f"https://randomuser.me/api/portraits/{gender}/{img_id}.jpg"

# Function to generate random Indian phone numbers (+91 followed by 10 digits)
def generate_phone_number():
    return f"+91 {random.randint(6000000000, 9999999999)}"

# Create an empty list to store the generated data
data = []

# Loop through the number of rows to generate names, phone numbers, and image URLs
for i in rows:
    name = fake.name()
    phone = generate_phone_number()
    image_url = generate_image_url()
    data.append([i, name, phone, image_url])

# Create a DataFrame to store the data
df = pd.DataFrame(data, columns=['Row Number', 'Owner Name', 'Phone', 'Image URL'])

# Saving to CSV (optional)
df.to_csv('random_owner_data.csv', index=False)
