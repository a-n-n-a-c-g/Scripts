numbervar=0
listoffinalnumbers=[]
while (numbervar<=999999):
    if (len(str(numbervar))<=6):
        zerovar="0"
        numberofzeros=6-(len(str(numbervar)))
        madezeros=zerovar*numberofzeros
        finalnumber=madezeros+str(numbervar)
        listoffinalnumbers.append(finalnumber) 
    numbervar+=1
with open('Lancessuccess.dict', 'w') as filetowrite:
    for listitem in listoffinalnumbers:
        filetowrite.write('%s\n' % listitem)
    filetowrite.close()
