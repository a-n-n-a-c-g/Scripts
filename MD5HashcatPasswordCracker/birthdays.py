listoffbirthdays=[]
monthvar=1
while monthvar<=12:
    dayvar=1
    while dayvar<=31:
        yearvar=2000
        while yearvar<=2014:
            birthday=(str(monthvar)+"/"+str(dayvar)+"/"+str(yearvar))
           # print birthday
            listoffbirthdays.append(birthday)
            yearvar+=1
        dayvar+=1
    monthvar+=1
with open ('birthdays.dict', 'w') as filetowrite:
    for listitem in listoffbirthdays:
        filetowrite.write('%s\n' % listitem)
    filetowrite.close()
