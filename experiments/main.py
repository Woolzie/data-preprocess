import pdfplumber
import pandas as pd
import os
import csv
import json

def extract_tables_from_pdf(filename):
    tables = []
    try:
        with pdfplumber.open(filename) as pdf:
            for page in pdf.pages:
                # Extract table assuming tables with borders
                table = page.extract_table()
                if table:
                    tables.append(table)
        return tables
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return None
def save_tables_as_csv(tables, filename):
    base_filename = os.path.splitext(filename)[0]
    csv_filenames = []
    for i, table in enumerate(tables):
        header = table[0]
        data = table[1:]
        df = pd.DataFrame(data, columns=header)
        csv_filename = f"{base_filename}_table_{i+1}.csv"
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
        print(f"Saved table {i+1} as {csv_filename}")
        csv_filenames.append(csv_filename)
    return csv_filenames


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # Read csv file
    with open(csvFilePath, encoding='utf-8', errors='ignore') as csvf:
        # Load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # Convert each csv row into python dict
        for row in csvReader:
            # Add this python dict to json array
            jsonArray.append(row)

    # Convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
    print(f"File '{jsonFilePath}' saved.")

if __name__ == "__main__":
    # Step 1: Extract tables from PDF and save as CSV
    pdf_filename = r"sample.pdf"  # Replace with your PDF file
    tables = extract_tables_from_pdf(pdf_filename)
    
    if tables:
        csv_filenames = save_tables_as_csv(tables, pdf_filename)

        # Step 2: Convert each CSV file to JSON
        for csv_filename in csv_filenames:
            json_filename = os.path.splitext(csv_filename)[0] + ".json"
            csv_to_json(csv_filename, json_filename)
    else:
        print("No tables found in the PDF.")