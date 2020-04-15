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
    elif (file_extension == ".txt"):
        text = open(file, "r").read()
    else:
        text = "I don't know this file type"
    text = re.sub('[^A-Za-z0-9\s]+', '', text)
    assignmentfile = open("../assignment.txt","w")
    assignmentfile.write(text)
    #print text
    return text

def recurseit():
    directory = "../Essays"
    for filename in os.listdir(directory):
        print (colored.WARNING + (filename) + colored.ENDC)
        theentiredamnthing(printtext(os.path.join(directory,filename)))
        raw_input("Copied to Clipboard. Press return to continue. \n\n")

def main():
    recurseit()

if __name__ == "__main__":
    main()
