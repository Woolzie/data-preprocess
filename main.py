'''
assumptions:- no sudden bold text in middle of text
'''
import fitz
import pymupdf
import spacy
import re
import statistics
from collections import Counter
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
    importance =[]
    for item in extract_data:
        font_size = int(item["font_size"]) * 1.5
        font_weight = item["font_weight"]
        importance_value = font_size + font_weight
    
    # Append as a dictionary
        importance.append({
            "importance": importance_value,
            "text": item["text"]
            })

    return importance
# use weighted mean to find the answer, for now 1.5:1, check later



                        
def detect_headings(extracted_data) :
    # sort by using the values obtained from Counter(importance)
    return 0

def jsonconvert():
    return 0
    

if __name__ ==  "__main__": 
    files =["phenol-liquid-cert-.pdf","hmm.pdf", "lorem.pdf"]
    data = extract_text_with_details(files[2])
    mean = findmean(data)
    print(mean)
    # print("big value: "+ str(max(mean)))
    # mode = statistics.mode(mean)
   # print(mode)
    #print("count: "+ str(Counter(mean)))

''' style:
when testing dont use print within the function, return the data and have it print in the main 
'''

