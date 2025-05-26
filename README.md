**GCP Employee Data ETL Pipeline**

**Data Generation:** A Python script leveraging Faker to create a CSV file of 100 synthetic employee records with fields such as name, job title, department, email, address, phone number, salary, and password.

**Cloud Storage Upload:** Upload of the generated CSV to a Google Cloud Storage (GCS) bucket using service account credentials.
**Big Query:** Creating table using CSV .
**Data Masking:** Data Fusion Wrangler is used to mask or obfuscate sensitive fields (e.g., email, phone number) before loading.
**BigQuery Load:** Loading the cleaned and masked data into a BigQuery table with a predefined schema.
**Visualization:** Connecting BigQuery to Power BI for reporting via Import or DirectQuery.


**Prerequisites:**

Google Cloud Project with billing enabled
Enabled APIs: Cloud Storage, Data Fusion, BigQuery, IAM
Service Account JSON key with roles:
    Storage Object Admin
    Data Fusion Developer
    BigQuery Data Editor


**Getting Started:**

**1. Install Dependencies**
Faker
google-cloud-storage

**2. Configure Credentials**
Place your service account key JSON somewhere safe and update the key_path in both Python scripts:
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/path/to/your-key.json"

**3. Extract data:**
Getting data using the Faker library.

**4. Generate data and upload to GCS**
python extract.py

**5. Mask Data in Data Fusion**
Follow instructions in df_masking_instructions.md to:
Launch Wrangler
Load employee_data.csv from GCS
Apply masking transforms (phone, password)
Export masked CSV back to GCS or stage.

**6. Load to BigQuery**
using a data fusion ETL pipeline to load data into BigQuery.

**7. Visualize in Power BI**
Use the native BigQuery connector in Power BI Desktop.
Choose Import to get data into Power BI
