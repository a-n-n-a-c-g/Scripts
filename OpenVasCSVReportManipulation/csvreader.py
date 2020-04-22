#TODO: sort by details and combine IPs with same details?
import csv
import sys, getopt
import os

def getinputs():
    reporter = input("Enter reporter's initials: ")
    team = input("Enter team: ")
    date = input("Enter date (dd Month yyyy) scan was run: ")
    return(reporter,team,date)

def readfile(inputfile):
    datalist=[]
    inputs = getinputs()
    with open(inputfile) as f:
        headers = next(f) #skip headers
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            hostlist = [] #all data from single host
            ipaddr = row[0] #used in host
            portnum = row[2] #used in host
            severity = row[5]
            summary = row[8] #used in details
            specresult = row[9] #used in details
            impact = row[16] #used in details
            vulninsight = row[18] #used in details
            reporter = inputs[0]
            team = inputs[1]
            date = inputs[2]

            if (portnum != ""): #check for port number
                host=(ipaddr+":"+portnum) #concat IP and port
            else:
                host=(ipaddr)
        
            details=(summary+" "+specresult+" "+impact+" "+vulninsight)
            details=details.replace('\n',' ') 
            details=details.replace('  ',' ')

            hostlist.append(host)
            hostlist.append(severity)
            hostlist.append(details)
            hostlist.append(reporter)
            hostlist.append(team)
            hostlist.append(date)

            datalist.append(hostlist)
        return(datalist)

def writefile(outputfile, datalist):
    if not (os.path.exists(outputfile)): #outputfile doesn't exist
        headers = ['host','criticality','details','reporter','team','date']
        datalist.insert(0, headers)
    with open(outputfile, 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerows(datalist)

def parse_file(inputfile="reportbak.csv",outputfile="outfile.csv"):
    writefile(outputfile,(readfile(inputfile)))
    return(outputfile)

if __name__ == "__main__":
    parse_file()
