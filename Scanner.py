import PyPDF2
import pandas as pd
import re
import io
import os
import urllib.request
from urllib.parse import urlparse
from os.path import exists
import warnings

 

switch = 0

# Ask the user for links or file paths

pii_elements = input("Enter the PII elements (comma-separated): ").split(',')

# pii_elements = ['BSCID', 'EMPLID', 'LAST_NAME', 'FIRST_NAME', 'EMAIL', 'NAME','SSN','Birth','DOB']

warnings.simplefilter(action='ignore', category=UserWarning)

excel = []


def detect_pii_in_pdf(pdf_path, pii_elements):

     req = urllib.request.Request(pdf_path, headers={'User-Agent' : "Magic Browser"})

     remote_file = urllib.request.urlopen(req).read()

     remote_file_bytes = io.BytesIO(remote_file)

     reader = PyPDF2.PdfReader(remote_file_bytes)

     for page_num in range(len(reader.pages)):

        page = reader.getPage(page_num)

        text = page.extractText()

             # Define regex patterns for partial matching of PII within words or longer strings

     pii_patterns = [rf'\b.*?{element}.*?\b' for element in pii_elements]


     for pattern in pii_patterns:

        matches = re.findall(pattern, text, flags=re.IGNORECASE)

        if matches:

            # print(f"PII found in PDF on page {page_num + 1}: {matches} in " + pdf_path)

            data = [page_num + 1,matches,pdf_path]

            excel.append(data)

            switch = 0

        else:

            switch = 1


def detect_pii_in_xlsx(xlsx_path, pii_elements):

     df = pd.read_excel(xlsx_path)

     # Define regex patterns for partial matching of PII within words or longer strings

     pii_patterns = [rf'\b.*?{element}.*?\b' for element in pii_elements]

     for column in df.columns:

         for pattern in pii_patterns:

             matches = df[column].astype(str).apply(lambda x: re.findall(pattern, x, flags=re.IGNORECASE))

             matches = [match for match_list in matches for match in match_list]

             if matches:

                 # print(f"PII found in XLSX in column '{column}': {matches} in " + xlsx_path)

                 data = [column,matches,xlsx_path]

                 excel.append(data)

                 switch = 0

             else:

                 switch = 1

def detect_pii_in_file(extracted_links, pii_elements):

    for file_path in extracted_links:

         if file_path.lower().endswith('.pdf'):

            detect_pii_in_pdf(file_path, pii_elements)    

         elif file_path.lower().endswith('.xls'):

            detect_pii_in_xlsx(file_path, pii_elements)

         elif file_path.lower().endswith('.xlsx'):

            detect_pii_in_xlsx(file_path, pii_elements)

         else:

          print(f"Unsupported file type: {file_path}")

 

# Detect PII in each user-provided link or file path


def extract_links_from_xlsx(xlsx_path):

     print("Wait checking the data")

     df = pd.read_excel(xlsx_path)

     # Define a regex pattern to extract links (accepts both http(s) URLs and file paths)

     link_pattern = r'(https?://[^\s]+)|(\S+\.\S+)'

     extracted_links = []

     # Iterate through all cells in the dataframe

     for column in df.columns:

         for index, cell_value in df[column].items():

             # Check if the cell value contains a link

             if isinstance(cell_value, str):

                 links = re.findall(link_pattern, cell_value)

                 extracted_links.extend([link[0] or link[1] for link in links if any(link)])

              

     return extracted_links

 

def extract_file_from_folder(folder_path):

  print("Wait checking the data")

  extracted_links = []

  file_name =  os.listdir(folder_path)

  for name in file_name:

        extracted_links.append(folder_path+"\\" + name)

  return extracted_links


user_input = input("Enter the links or file paths: ")


if user_input.lower().endswith('.xlsx'):

    detect_pii_in_file(extract_links_from_xlsx(user_input), pii_elements)

else:

    detect_pii_in_file(extract_file_from_folder(user_input), pii_elements)


user_input = input("Enter your userID ")

fileName = input("Name the file")

pd.DataFrame(excel,columns=['Column name', 'Matches', 'Link/File Path']).to_excel('C:\\Users\\'+ user_input +'\\Downloads\\'+fileName+'.xlsx')

print('Process Completed, Check your Downloads Folder')
