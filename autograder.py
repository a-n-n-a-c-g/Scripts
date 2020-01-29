import os
from time import sleep
#os.system('clear')
class colored:
    WARNING = '\033[91m'    
    ENDC = '\033[0m'

newfile = open("../assignment.txt","r")

def theentiredamnthing(newfile):
    word = ["test", "testhi"]
    word1 = ["this is a test", "suppp"]
    word2 = ["what's up test"]
    listofwordlists = [word,word1,word2]
    wordlisttitles = ["Title1","Title2","Title3"]
    os.remove('../grade.txt')
    counterOfWords = 0
    CounterofZeroes = 0
    for line in newfile:
        line = line.lower()
        listnumber = 0
        for listnumber in range(len(listofwordlists)):
            i = 0
            currentlist = listofwordlists[listnumber]
            for i in range(len(currentlist)):
                newestword = currentlist[i]
                lowerword = newestword.lower()
                if (currentlist[i] == "0"):
                        continue
                elif (currentlist[i] in line):
                    del currentlist[i]
                    currentlist.insert(i,"0")
                    i+=1
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

def main():
    theentiredamnthing(open("../assignment.txt","r"))
    newfile.close()

if __name__ == "__main__":
    main()
