from faker import Faker
from reportlab.pdfgen import canvas
import pandas as pd

fake = Faker()

# Function to generate fake PII data
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

# Function to create Excel file with fake PII data
def create_excel(fake_data):
    excel_filename = 'fake_pii_data.xlsx'
    
    # Convert data to DataFrame
    df = pd.DataFrame(fake_data)
    
    # Write DataFrame to Excel file
    df.to_excel(excel_filename, index=False, engine='openpyxl')

    print(f"Excel file '{excel_filename}' created successfully.")

# Function to create PDF with fake PII data
def create_pdf(fake_data):
    pdf_filename = 'fake_pii_data.pdf'
    
    with canvas.Canvas(pdf_filename) as pdf:
        pdf.setTitle("Fake PII Data")
        
        # Set font
        pdf.setFont("Helvetica", 12)
        
        # Add PII data to the PDF
        for record in fake_data:
            for key, value in record.items():
                pdf.drawString(50, pdf._pagesize[1] - 50, f"{key}: {value}")
                pdf.translate(0, -15)  # Move down for the next line
            pdf.translate(0, -20)  # Add extra space between records

    print(f"PDF file '{pdf_filename}' created successfully.")

# Generate fake data
fake_data = generate_fake_data(num_records=5)

# Create Excel file with fake data
create_excel(fake_data)

# Create PDF with fake data
create_pdf(fake_data)
