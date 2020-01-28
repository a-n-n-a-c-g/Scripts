word = ["Anna","Hello","Sup ","Hi"]
word1 = ["ugh","test"]
word2 = ["this is a test", "suppp"]
listofwordlists = [word,word1,word2]
newfile = open("../assignment.txt","r")
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
            if (currentlist[i] in line) or (lowerword in line):
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
    percentagemissed = (100*(int(wordsmissed)) / (int(totalwords)))
    print currentlist
    print str(wordsmissed) + " words missed in word" + str(entry) + " = "  + str(percentagemissed) + "%"
newfile.close()
