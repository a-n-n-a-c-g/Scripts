import os, glob, shutil
           
def main():
    list = []
    for filename in os.listdir('vmdk-descriptorfiles'):  
        char ='"'
        file = open("vmdk-descriptorfiles/" + filename, "r")
        for line in file:
            if "RW" in line:
                #print "crap"
                begin = 0
                end = 0
                begin = (int)(line.find(char)) + 1
                end = (int)(line.find(char, begin+1))
                newfilename = str(line[int(begin):int(end)])
                #list.append(newfilename)
                #if "flat" in line:
                newfilename = newfilename.replace('-flat', '')
                #if "delta" in line:
                newfilename = newfilename.replace('-delta', '')
                newfilename = newfilename.replace('.txt', '')

                #list.append(newfilename)
                #print newfilename
                
                ourflag = False
                counter = 0
                newfilename = "fixed-vmdk-descriptorfiles/" + newfilename
                newnewfilename = newfilename + ".txt"

                while ourflag != True:
                    if (os.path.isfile(newnewfilename)) == False:
                        print filename + " -> " + newnewfilename
                        #print newnewfilename
                        shutil.copy2("vmdk-descriptorfiles/" + filename, newnewfilename)
                        ourflag = True
                    else:
                        counter+=1
                        newnewfilename = str(newfilename + "-" + str(counter) + ".txt")
 
                #renamefile(newfilename, filename, 0)   
        uniquelist = set(list)
    print len(list)
    print len(uniquelist)

if __name__ == "__main__":
   main()

