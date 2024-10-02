

'''
1. test  the difference between sort=true and false within the get_text() 
    by comparing 
2. test own pdfs
3. convert the things into json by comparing importance 

'''
import fitz
import pymupdf

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
                            "page": page_num,
                            "bbox": span.get("bbox")

                        })
    return extracted_data


def findmean(extract_data):
    
    importance =[]
    for item in extract_data:
        # size.append(item["font_size"])
        # weights.append(item["font_weight"])
        importance.append(int(item["font_size"])*1.5 + item["font_weight"])
    return importance
# use weighted mean to find the answer, for now 2:1, check later



def testfunc(files, mean):
    x=0
    for data in files:
        text= data["text"]
        size =data["font_size"]
        wgt = data["font_weight"]
        bbox = data["bbox"]
        print(f"text: {text} font-size:{size} font-weight: {wgt}", end=" ")
        print(f" importance : {mean[x]}", end="\n---")
        print(f"\t\tbbox values: tr{bbox[0]}, {bbox[1]}, bl {bbox[2]}, {bbox[3]}", end="\n====\n")
        x+=1
    print("value of x is "+ str(x))


if __name__ == "__main__":
    files =["phenol-liquid-cert-.pdf","hmm.pdf"]
    data = extract_text_with_details(files[1])
    mean = findmean(data)
    testfunc(data,mean)

'''
conclusion:- 
text on the same line will be considered different when the font size and font weight changes 
1.  problem :- just to highlight a word, this could be bad cuz the text will be considered different (a new key-value)
           pair would be generated
    fix : incorporate bbox and look for how far the prev word is, as long as its a space, it will be fine

'''