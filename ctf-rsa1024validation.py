import os
directory = "."
numberofbadfiles = 0
numberoftotalfiles = 0
listoffilenames = []
for filename in os.listdir(directory):
    #print(filename)
    filenamebegin = os.path.splitext(filename)[0]
    #print "made it here"
    if filenamebegin in listoffilenames:
        listoffilenames.remove(filenamebegin)
        #print("removed")
    else:
        listoffilenames.append(filenamebegin)
        #print("added")
print listoffilenames

for filename in os.listdir(directory):
    #print filename
    if filename.endswith(".pub"):
        numberoftotalfiles+=1
        #should be pub format
        #print("pub")
        with open(filename,'r') as f:
            data=f.read().strip()
            #print data
            number = len(data)
            beginning = data[:8] # "ssh-rsa "
            end = data[-16:] # " root@blackpearl"
            middle = data[8:-16]
            lenofkey=len(middle)
            #print lenofkey
            if (lenofkey != 200): 
                print filename
                print lenofkey
                print("bad keylen")
                #input("I see.....")
                numberofbadfiles+=1
                continue
            elif (beginning != "ssh-rsa "):
                print filename
                print("bad beg")
                #input("I see.........")
                continue
            elif (end != " root@blackpearl"):
                print filename
                print ("bad end")
                #input("I see.............")
                continue
            elif (number != 224):
                print filename
                print("bad file length")
                #input("I see................")
                continue
            else:
                continue
        f.close()
        #print("fine")
    elif filename.endswith(".py"):
        continue
    else:
        #should be priv format
        #print ("priv")
        numberoftotalfiles+=1
        with open(filename,'r') as f:
            data=f.read().strip()
            #print data
            number = len(data)
            beginning = data[:31] 
            end = data[-29:] 
            middle = data[32:-30]
            lenofkey=len(middle)
            if ((lenofkey != 824) and (lenofkey != 820)): 
                print filename
                print lenofkey
                print("bad keylen")
                numberofbadfiles+=1
                continue
                #input("I see.....")
            elif (beginning != "-----BEGIN RSA PRIVATE KEY-----"):
                print filename
                print("bad beg")
                #input("I see.........")
                continue
            elif (end != "-----END RSA PRIVATE KEY-----"):
                print filename
                print ("bad end")
                continue
                #input("I see.............")
            elif ((number != 886) and (number != 882)):
                print filename
                print number
                print("bad file length")
                continue
                #input("I see................")
            else:
                continue
                #print("fine")
        f.close()
        #print ("Priv")
        #print beginning
        #print end
        #print lenofkey
        #print middle
        #print number
print("number of bad files: " + str(numberofbadfiles))
print("total files: " + str(numberoftotalfiles))
