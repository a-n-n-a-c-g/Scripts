import os
class colored:
    WARNING = '\033[91m'    
    ENDC = '\033[0m'
word = ["Hiding", "Confidential", "Private", "Sensitive", "Public", "Data Loss Prevention", "Identity And Access Management", "Data at Rest", "Data in Transit", "Data in Use", "Marking", "Data remanence", "Erasing", "Clearing", "Purging", "Degaussing", "Destruction", "Declassification", "Record retention", "Symmetric", "Transport encryption", "Data processor", "Pseudinymization", "Anonymization", "Scoping", "Tailoring"]
word1 = ["Trusted Computing Base", "Security Perimeter", "Reference Monitor", "State Machine", "Information Flow", "Noninterference", "Take-Grant", "Access Control Matrix", "Bell-LaPadula", "Biba", "Clark-Wilson", "Brewer and Nash"]
word2 = ["Confidentiality", "Integrity", "Nonrepudiation", "Availability", "Identification", "Authentication","Authorization", "Audit", "Account", "Layering", "Abstraction", "Separation of duties", "Collusion","Security policy", "Acceptable use policy", "Baseline", "Compliance", "Privacy", "Security governance","COBIT"]
listofwordlists = [word,word1,word2]
wordlisttitles = ["Data Protection","Security Models","Policies"]
newfile = open("../assignment.txt","r")
os.system("clear")
os.remove('../grade.txt')
counterOfWords = 0
CounterofZeroes = 0
for line in newfile:
    #print "line #" + line
    #print word
    listnumber = 0
    for listnumber in range(len(listofwordlists)):
        i = 0
        currentlist = listofwordlists[listnumber]
        #ZeroesinCurrentList = 0
        for i in range(len(currentlist)):
            newestword = currentlist[i]
            lowerword = newestword.lower()
            if (currentlist[i] == "0"):
                    continue
            elif (currentlist[i] in line) or (lowerword in line):
                #print "success"
                del currentlist[i]
                #print word
                currentlist.insert(i,"0")
                i+=1
                #ZeroesinCurrentList += 1
        #print currentlist 
        #CounterofZeroes+=ZeroesinCurrentList
        #print ZeroesinCurrentList 
        #print CounterofZeroes
for entry in range(len(listofwordlists)):
    currentlist = listofwordlists[entry]
    totalwords =  len(currentlist)
    numberofZeroes = 0
    i = 0
    for i in range(len(currentlist)):
        if currentlist[i] == "0":
            numberofZeroes+=1
        i+=1
    wordsmissed = totalwords - numberofZeroes
    percentagegotten = (100*(int(numberofZeroes)) / (int(totalwords)))
    #print currentlist
    print (colored.WARNING + (str(wordsmissed) + " words missed out of "+ str(totalwords) +" in " + str(wordlisttitles[entry]) + " = "  + str(percentagegotten) + "% included") + colored.ENDC)
    while "0" in currentlist: currentlist.remove("0")
    print(currentlist)
    gradingfile = open('../grade.txt','a')
    gradingfile.write("You missed the following required words in " + str(wordlisttitles[entry]) + ":\n")
    gradingfile.write(str(currentlist)+"\n")
    gradingfile.write("You got " + str(numberofZeroes) + " words out of " + str(totalwords) + " in this topic")
    gradingfile.write("\n\n")
    gradingfile.close()
os.system("cat ../grade.txt | clip.exe")
newfile.close()
