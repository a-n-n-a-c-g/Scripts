import psutil
import time

print ("Current Memory Used:")
memuse = psutil.virtual_memory().percent
print(memuse)

print("Total CPU Load: ")
cpuload = psutil.cpu_percent()
print(cpuload)

print("CPU Load / Core: ")
loadpercore = int(psutil.cpu_percent()) / int(psutil.cpu_count())
print(loadpercore)

print ("Number of Cores: ")
cores = psutil.cpu_count()
print(cores)

print("Swap Percent Used: ")
swappercent = psutil.swap_memory().percent
print(swappercent)

print("24-Hour Logins: ")
epoch_time = int(time.time())
last24hours = int(epoch_time) - 86400
numofusers = len(psutil.users())
users = [numofusers]
for i in range(numofusers):
    if (psutil.users()[i].started <= last24hours):
        users[i] = psutil.users()[i].name
print(*users)

# print to a file
file = open("/var/log/hostinfo.csv","w")
file.write(str(memuse) + " , " + str(cpuload) + " , " + str(loadpercore) + " , " + str(cores) + " , " + str(swappercent) + " , " + str(users))
file.close()
