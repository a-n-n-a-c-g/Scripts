# OpenVas CSV Report Manipulation
## csvreader.py
- does most of the file parsing. Can be run alone, but, if you do so, change the input file (it's currently reportbak.csv)
- accepts input for date/reporter/team/etc
- writes results to outfile.csv
## csvwrapper.py
- wrapper for csvreader.py
- allows you to run the program on a directory (it looks for csv files recursively in the given directory)
- allows you to write out to a file
- asks if you want to sort your results, uses csvsorter.py and prints results, sorted by vulnerability, to sorted-whateverYourOutputFileWasNamed.
## csvsorter.py
- accepts an input file (reads from outfile.csv if run by itself)
- searches through the file for identical details about vulnerabilities and combines the rest of the info based on this detail match.
- uses csvreader.py to write out to a file (out.csv)
