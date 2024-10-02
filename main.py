'''
assumptions:- no sudden bold text in middle of text
TODo:
1. handle : that are in the string
    use of \: to make it work
2. have the smaller data (mode) be inside lists
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
    # iterate through the data and insert \ when : is there
    # for i in ans:
    #     temp=""
    #     if i==':':
    #         temp=ans
    if pos==0:
        ans+="{'"+data+"':"
    else :
        size= len(data)
        x=0
        for i in range(size-1,1,-1):
            prev=data[i-1]
            if prev+data[i] != "\:":
                ans+="},"
                x+=1
            elif x>pos:
                break;  
            else :
                continue
    return ans           
def cleanofcolon(data):
    size=len(data)
    for i in range(1,size,2):
        text= data[i]
        text=text.replace(":","\:")
    return data
def stack(data):
    stack = [data[0]]
    # assuming the first text to be the title 
    top=0
    # find out the smallest data so it can be in list 
    mode = statistics.mode(data)
    size= len(data)
    ans = "{'"+data[1]+ "':"
    isStart = True
    for i in range(2,size,2):
        text=data[i+1]
        imp = data[i]
        if ans[-1]!= ":":
            ans+="' ]"
            isStart= False
        else :
            None
        if i<=stack[top]:
            stack.append(imp)
            top+=1
            ans=insertdata(ans,text,0)
        elif data[i]== mode:
            if isStart:
                ans+= "[ '"+text
            else :
                ans += ", "+ text
            isStart= True
        else :
            x=0
            # not sure about the comparison
            while stack[top]<= imp and top>0:
                stack.pop()
                top-=1
                x+=1
            # now for the appendings part 
            ans=insertdata(ans,text,x)
        # if ans[-1]==",":
        #     if
            # pop and update the value of ans
    return ans

def parsejson(data):
    return json.loads(data)

# shouldnt i sort and see create the appropriate {{[]}}
if __name__ ==  "__main__": 
    files =["phenol-liquid-cert-.pdf","hmm.pdf", "lorem.pdf"]
    data = extract_text_with_details(files[2])
    mean = cleanofcolon(findmean(data))
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

