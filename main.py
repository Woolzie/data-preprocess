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
    imp =[]
    x=0
    for item in extract_data:
        font_size = int(item["font_size"]) * 1.5
        font_weight = item["font_weight"]
        importance_value = font_size + font_weight
        x+=1
    # Append as a dictionary
        imp.append({x:[item["text"],importance_value]})

    return imp
# use weighted mean to find the answer, for now 1.5:1, check later



                        
def detect_headings(extracted_data) :
    # sort by using the values obtained from Counter(importance)
    return 0

# def nestbyimp(data):
#     # considering the heading to be the first
#     current_imp= data[0]["imp"]
#     current_data =data[0]["text"]
#     ans = {current_data:[{}]}

#     for item in data[1:]:
#      if item["imp"]<=current_imp:
#        # move inside its values,
#        return


    # find mode and max values
def nestbyimp(data):
    current = data[0]
    ans={}
    # if current[1]
    i = 2
    x=2
    for item in data[1:]:
        prev = current
        current=item
        nex = data[i]
        if current[x][1]> 30:
            print(current[x][0])
        x+=1
        #if 
        
# shouldnt i sort and see create the appropriate {{[]}}
if __name__ ==  "__main__": 
    files =["phenol-liquid-cert-.pdf","hmm.pdf", "lorem.pdf"]
    data = extract_text_with_details(files[2])
    mean = findmean(data)
    #print(mean)
    #print(mean[0][1][1])
    # print("big value: "+ str(max(mean)))
    # mode = statistics.mode(mean)
   # print(mode)
    #print("count: "+ str(Counter(mean)))
    nestbyimp(mean)
''' style:
when testing dont use print within the function, return the data and have it print in the main 
'''

