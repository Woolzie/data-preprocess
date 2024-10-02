

import fitz
import pymupdf
import spacy
import re
import statistics

nlp = spacy.load("en_core_web_sm")

def extract_text_with_details(file_path):
    doc = fitz.open(file_path)
    extracted_data = []
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict", sort=True)["blocks"]
        for block in blocks:
            if block['type'] == 0:  # text block
                for line in block["lines"]:
                    for span in line["spans"]:
                        extracted_data.append({
                            "text": span["text"],
                            "font_size": span["size"],
                            "font_weight": span["flags"],
                            "page": page_num
                        })
    return extracted_data

def findmean(extract_data):
    size = []
    weights= []
    importance =[]
    for item in extract_data:
        # size.append(item["font_size"])
        # weights.append(item["font_weight"])
        importance.append(int(item["font_size"])*1.5 + item["font_weight"])
    return importance
# use weighted mean to find the answer, for now 2:1, check later



                        
def detect_headings(extracted_data) :
    headings = []
    subheadings = []
    font_list =[]
    for item in extracted_data:
        text = item["text"].strip()
        if not text:
            continue
        font_list.append(item["font_size"])
        # Heuristic based on font size and weight
        if item["font_size"] > 14 and item["font_weight"] >= 2:  # bold
            headings.append(text)
        elif item["font_size"] > 12 and item["font_weight"] >= 2:
            subheadings.append(text)
        else:
            continue

    return headings, subheadings, font_list

if __name__ ==  "__main__": 
    files =["phenol-liquid-cert-.pdf","hmm.pdf"]
    data = extract_text_with_details(files[0])
    mean = findmean(data)
    print("big value: "+ str(max(mean)))
    mode = statistics.mode(mean)
    print(mode)

''' style:
when testing dont use print within the function, return the data and have it print in the main 
'''

