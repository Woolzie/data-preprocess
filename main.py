'''
assumptions:- no sudden bold text in middle of text
'''
import fitz
import pymupdf
import re
import statistics
from collections import Counter
import numpy 
import json

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
                        })
    return extracted_data

def findmean(extract_data):
    #{num:string}
    imp =[]
    x=0
    for item in extract_data:
        font_size = int(item["font_size"]) * 1.5
        font_weight = item["font_weight"]
        importance_value = font_size + font_weight
        imp.append(importance_value)
        imp.append(item["text"])
        # x+=2
    # # Append as a dictionary
    #     imp.append({x:[item["text"],importance_value]})

    return imp
# use weighted mean to find the answer, for now 1.5:1, check later
def insertdata(ans,data,pos):
    index=0
    if pos==0:
        ans+="{'"+data+"':"
    else :
        size= len(ans)
        x=0
        for i in range(size-1,0,-1):
            if i==':':
                ans+="},"
                x+=1
            elif x>pos:
                break;  
            else :
                continue
    return ans           


def stack(data):
    stack = [data[0]]
    # assuming the first text to be the title 
    top=0
    # find out the smallest data so it can be in list 
    mode = statistics.mode(data)
    size= len(data)
    ans = "{'"+data[1]+ "':"
    for i in range(2,size,2):
        if i<=stack[top]:
            stack.append(data[i])
            top+=1
            ans=insertdata(ans,data[i+1],0)
        else :
            x=0
            # not sure about the comparison
            while stack[top]<= data[i] and top>0:
                stack.pop()
                top-=1
                x+=1
            # now for the appendings part 
            ans=insertdata(ans,data[i+1],x)
                
            # pop and update the value of ans
    return ans
        


                        
def detect_headings(extracted_data) :
    # sort by using the values obtained from Counter(importance)
    return 0



    # find mode and max values
def nestbyimp(data,small):
    x=2
    ans="{'"
    for item in data[1:]:
        prev = current
        current=item
        nex = data[i]

        if current[x][1]> prev[x-1][1]:
            return
            # append or something


        # elif current[x][1] == small:
        #     # create a list and append 
        #      return
        # else current[x][1] :
            
        
        #if import spacy

def parsejson(data):
    return json.loads(data)

# shouldnt i sort and see create the appropriate {{[]}}
if __name__ ==  "__main__": 
    files =["phenol-liquid-cert-.pdf","hmm.pdf", "lorem.pdf"]
    data = extract_text_with_details(files[2])
    mean = findmean(data)
    ans = stack(mean)
    print(ans)
    #print(mean[0][1][1])
    # print("big value: "+ str(max(mean)))
    # mode = statistics.mode(mean)
   # print(mode)
    #print("count: "+ str(Counter(mean)))
    # nestbyimp(mean,small)
''' style:
when testing dont use print within the function, return the data and have it print in the main 
'''

