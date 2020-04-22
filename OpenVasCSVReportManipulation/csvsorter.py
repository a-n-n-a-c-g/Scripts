import csv
from csvreader import writefile

def readfile(inputfile):
    with open(inputfile) as f:
        headers=next(f)
        reader=csv.reader(f,delimiter=",")
        hosts=[]
        severitys=[]
        details=[]
        reporters=[]
        teams=[]
        dates=[]
        for row in reader:
            hosts.append(row[0]) #3. pull this 
            severitys.append(row[1]) #2. make sure this is the same
            detail = row[2] #1. check if same
            reporters.append(row[3]) #4. if not same, append. If same, leave
            teams.append(row[4]) #see 4
            dates.append(row[5]) #see 4
            details.append(detail)
        
        sort_file(hosts,severitys, details, reporters,teams,dates)
        
def sort_file(hosts,severitys,details,reporters,teams,dates):
    sortedlist=[]
    uniquedetails=[]
    for i in (range(0,(len(details)))):
        if not details[i] in uniquedetails:
            uniquedetails.append(details[i])
    for i in (range(0,(len(uniquedetails)))):
        uniquedetail = uniquedetails[i]
        indeces = [index for index, value in enumerate(details) if value == uniquedetail]
        #print("uniquedetails at spot "+ str(i) + ": " + str(indeces))
        duplicatehosts = []
        testcrap = []

        #the next 4 lines assume that if a description is the same the rest of the stuff is the same
        duplicateseveritys = severitys[indeces[0]]
        duplicatereporters = reporters[indeces[0]]
        duplicateteams = teams[indeces[0]]
        duplicatedates = dates[indeces[0]]
        
        for j in (range(0,(len(indeces)))):
            indextoget = indeces[j]
            duplicatehosts.append(hosts[indextoget]) 
        
        testcrap.append(duplicatehosts)
        testcrap.append(duplicateseveritys)
        testcrap.append(uniquedetails[i])
        testcrap.append(duplicatereporters)
        testcrap.append(duplicateteams)
        testcrap.append(duplicatedates)
        
        sortedlist.append(testcrap)
    #print(sortedlist)
    writefile("out.csv",sortedlist)

if __name__ == "__main__":
   readfile("outfile.csv")
