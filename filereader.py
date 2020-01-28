import docxpy
import os
from io import StringIO
from pdfminer.high_level import extract_text
from autograder import theentiredamnthing

#recursively go through files
#get filenames
def printtext(file):
#file = "C:/Users/annac/Code/file.pdf"
    file_name, file_extension = os.path.splitext(file)
    junk, filenamenopath = os.path.split(file_name)
    #print filenamenopath
    filename = file_name+".txt"
    if (file_extension == ".docx"):
        text = docxpy.process(file)
        doc = docxpy.DOCReader(file)
        doc.process()  # process file
        #print text
        #print "word doc"
    elif (file_extension == ".pdf"):
        text = extract_text(file)
        #print(text)
        #print "pdf"
    else:
        text = "I don't know this file type"
    #print filenamenopath
    return text
    sleep(1000) 

def main():
    returnedtext = printtext("C:/Users/annac/Code/file.pdf")
    theentiredamnthing(returnedtext)

if __name__ == "__main__":
    main()
