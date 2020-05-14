#run as python3 csvwrapper.py <filepath> --outputDirectory <filepath>

import fnmatch
import argparse
import sys
import os
from csvreader import parse_file, writefile
from csvsorter import readfiletosort

def create_arg_parser():
    parser = argparse.ArgumentParser(description='These scripts parse OpenVas CSV scan results')
    parser.add_argument('inputDirectory',
                    help='Path to the input directory.')
    parser.add_argument('-o',
                    help='Path to the output that contains the resumes.')
    return parser

def checkinputtype(inputfile,outputfile):
    if(os.path.exists(inputfile)):
        if(os.path.isfile(inputfile)): #file was input
            filewasinput(inputfile,outputfile)
        elif(os.path.isdir(inputfile)): #directory was input
            directorywasinput(inputfile,outputfile)
        else: #neither file nor directory
            print("invalid file input")
    else: #path doesn't exist
        print("That file doesn't exist")

def checkoutputfile(enteredoutputfile):
    if(enteredoutputfile != None):
        if not enteredoutputfile.lower().endswith('csv'):
            outputfile=enteredoutputfile+".csv"
        else:
            outputfile=enteredoutputfile
    else: #no output file selected
        outputfile=None
    return(outputfile)

def filewasinput(inputfile,outputfile):
    print(inputfile)
    if outputfile==None:
        outputfile=parse_file(inputfile)
    else:
        outputfile=parse_file(inputfile,outputfile)
    print("Results from "+inputfile+" were printed to "+ outputfile)

def directorywasinput(inputfile,outputfile):
    for root, dirnames, filenames in os.walk(inputfile):
        for filename in fnmatch.filter(filenames, '*.csv'):
            inputfile=(os.path.join(root,filename))
            filewasinput(inputfile, outputfile)

def sort(outputfile):
    sort = input("Do you want to sort these results by vulnerability? (y|n): ")
    if(sort=="y"):
        sortedfile="sorted-"+outputfile
        print("Results will be sorted and printed to "+sortedfile)
        writefile(sortedfile,(readfiletosort(outputfile)))
    elif(sort=="n"):
        print("Results will not be sorted.")
    else:
        print("Sorry, did not understand input. Results will not be sorted.")

def main():
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    inputfile = parsed_args.inputDirectory
    enteredoutputfile = parsed_args.o
    outputfile=(checkoutputfile(enteredoutputfile)) #check if outfile exists
    checkinputtype(inputfile,outputfile) #check if dir or file in inputfile
    sort(outputfile) #sort results if desired

if __name__ == "__main__":
        main()
