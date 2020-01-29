import docxpy
import os
from io import StringIO
from pdfminer.high_level import extract_text
from autograder import theentiredamnthing
import re

class colored:
   WARNING = '\033[0;33m'    
   ENDC = '\033[0m'

def printtext(file):
    file_name, file_extension = os.path.splitext(file)
    junk, filenamenopath = os.path.split(file_name)
    filename = file_name+".txt"
    if (file_extension == ".docx"):
        text = docxpy.process(file)
        doc = docxpy.DOCReader(file)
        doc.process()  # process file
    elif (file_extension == ".pdf"):
        text = extract_text(file)
    else:
        text = "I don't know this file type"
    text = re.sub('[^A-Za-z0-9]+', '', text)
    return text
    sleep(1000) 

def recurseit():
    directory = "../Essays"
    for filename in os.listdir(directory):
        print ("\n\n" + colored.WARNING + (filename) + colored.ENDC)
        if filename.endswith(".pdf") or filename.endswith(".docx"):
            theentiredamnthing(printtext(os.path.join(directory,filename)))
            raw_input("Copied to Clipboard. Press return to continue.")
        else:
            continue

def main():
    recurseit()

if __name__ == "__main__":
    main()
