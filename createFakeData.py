from faker import Faker
from reportlab.pdfgen import canvas
import pandas as pd

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
    with canvas.Canvas(pdf_filename) as pdf:
        pdf.setTitle("Fake PII Data")
        pdf.setFont("Helvetica", 12)

        for record in fake_data:
            for key, value in record.items():
                pdf.drawString(50, pdf._pagesize[1] - 50, f"{key}: {value}")
                pdf.translate(0, -15)
            pdf.translate(0, -20)

    print(f"PDF file '{pdf_filename}' created successfully.")

# Example usage
num_records = 5
fake_data = generate_fake_data(num_records=num_records)

create_excel(fake_data)
create_pdf(fake_data)
