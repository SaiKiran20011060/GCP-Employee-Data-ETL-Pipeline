import csv
from faker import Faker
import random
import string
import os
from google.cloud import storage
from google.oauth2 import service_account

# === 1. GCP Authentication ===
# Replace with your actual service account key path
key_path = r"C:\Users\saiki\OneDrive\Desktop\SAI\Projects\Data Engineer\myfirstdata-460606-0cd355ca65d7.json"

# Set environment variable (optional if you use explicit credentials below)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

credentials = service_account.Credentials.from_service_account_file(key_path)

# === 2. Generate Fake Employee Data ===
num_employees = 100
fake = Faker()
password_characters = string.ascii_letters + string.digits + 'm'

with open('employee_data.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['first_name', 'last_name', 'job_title', 'department', 'email', 'address', 'phone_number', 'salary', 'password']
    writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    
    writer.writeheader()
    for _ in range(num_employees):
        writer.writerow({
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "job_title": fake.job(),
            "department": fake.job(),  # or use a custom department list if needed
            "email": fake.email(),
            "address": fake.city(),
            "phone_number": fake.phone_number(),
            "salary": fake.random_number(digits=5),
            "password": ''.join(random.choice(password_characters) for _ in range(8))
        })

# === 3. Upload CSV to GCS ===
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    client = storage.Client(credentials=credentials)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    print(f'File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}.')


bucket_name = 'empdata001'
source_file_name = 'employee_data.csv'
destination_blob_name = 'employee_data.csv'


upload_to_gcs(bucket_name, source_file_name, destination_blob_name)






















