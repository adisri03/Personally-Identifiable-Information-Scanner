from faker import Faker
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

fake = Faker()

def generate_fake_data(num_records=10):
    data = []

    for _ in range(num_records):
        record = {
            'First Name': fake.first_name(),
            'Last Name': fake.last_name(),
            'Email': fake.email(),
            'Phone Number': fake.phone_number(),
            'Address': fake.address(),
            'Date of Birth': fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d'),
            'Social Security Number': fake.ssn(),
        }
        data.append(record)

    return data

def create_excel(fake_data, excel_filename='fake_pii_data.xlsx'):
    df = pd.DataFrame(fake_data)
    df.to_excel(excel_filename, index=False, engine='openpyxl')
    print(f"Excel file '{excel_filename}' created successfully.")

def create_pdf(fake_data, pdf_filename='fake_pii_data.pdf'):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter

    c.setTitle("Fake PII Data")
    c.setFont("Helvetica", 12)

    for record in fake_data:
        for key, value in record.items():
            c.drawString(50, height - 50, f"{key}: {value}")
            c.translate(0, -15)
        c.translate(0, -20)

    c.save()
    print(f"PDF file '{pdf_filename}' created successfully.")

# Example usage
num_records = 5
fake_data = generate_fake_data(num_records=num_records)

create_excel(fake_data)
create_pdf(fake_data)
