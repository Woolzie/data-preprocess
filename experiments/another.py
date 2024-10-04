import pdfplumber
import json
import re

def extract_text_from_pdf_plumber(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            text += page_text + "\n"
    return text

def load_patterns(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def parse_sds_text(text, patterns):
    sds_dict = {}

    for section, field_patterns in patterns.items():
        sds_dict[section] = {}
        for field, pattern in field_patterns.items():
            match = re.search(pattern, text)
            if match:
                sds_dict[section][field] = match.group(1).strip()

    return sds_dict

pdf_path = "sample.pdf"
extracted_text = extract_text_from_pdf_plumber(pdf_path)

config_path = "config.json"
section_patterns = load_patterns(config_path)

sds_data = parse_sds_text(extracted_text, section_patterns)

json_filename = "sds_data.json"
with open(json_filename, 'w') as json_file:
    json.dump(sds_data, json_file, indent=4)

print(f"JSON data successfully saved to {json_filename}")