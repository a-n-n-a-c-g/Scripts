# Helpful one-liners

## AWS
- ```aws iam create-role --role-name vmimport --asume-role-policy -document file://Code/trust-policy.json```
- ```aws iam put-role-policy --role-name vmimport --policy-name vmimport --policy-document file://Code/role-policy.json```
- ```aws ec2 import-image --description "Gotham" --license-type BYOL --disk-containers file://Code/containers.json```
- ```aws ec2 describe-import-image-tasks --import-task-ids import-ami-amiIDnumber```

## Bash
### File Manipulation
- Find lines in file2 that aren't in file1: ```comm -13 <(sort -u file1.txt) <(sort -u file2.txt)```
- Count number of unique lines in a file: ```sort hosts.txt | uniq -c | wc -l```

### Network
- For when you don't have internet but someone else does (https://github.com/txthinking/brook): ```./brook client -l 127.0.0.1:8080 -i 127.0.0.1 -s <box with internet IP>:8080 -p password --http```

### Process Manipulation
- ```systemctl list-unit-files | grep enabled```
- ```systemctl | grep running```
- kill a process that keeps restarting:
  - ```ps -elf | grep "clock"```
  - ```grep -iRl "usr/local/bin/clock" /etc/```
  - ```systemctl stop clock.service (or disable)```
  - Make it immutable: ```chattr +i clock```
  - Check if it's immutable: ```lsattr```
  - Get rid of immutable: ```chattr -i clock```
    - Note: Can be helpful to chattr shadow file and then rename/move chattr (and any other linux commands you want) from ```sbin``` to confuse people
  
### Scheduled tasks
- List crontabs for every user: ```for user in $(getent passwd | cut -f1 -d: ); do echo $user; crontab -u $user -l; done```

## Cmd
- Direct diagnostic tool for PC info: ```dxdiag```

## Powershell
### Firewall/Network
- ```new-netfirewallrule -DisplayName "Testing TCP/80" -Direction Inbound -LocalPort 80 -Protocol TCP -Action Allow ```
- ```remove-netfirewallrule -DisplayName "Testing TCP/80"```
- ```route add 192.168.0.0 MASK 255.255.0.0 192.168.230.1 METRIC 5```
- ```route delete 192.168.0.0 MASK 255.255.0.0 192.168.230.1 METRIC 5 ```

### Scheduled tasks
- ```schtasks /create /tn myTask /tr "powershell -NoLogo -WindowStyle Hidden -file myScript.ps1" /sc minute /mo 1 /ru System ```
### Uninstall updates
- ```Get-Hotfix |where -Property InstalledOn -gt (get-date -date 01-01-2017)|%{ $sUpdate=$_.HotFixID.Replace("KB",""); write-host ("Uninstalling update "+$sUpdate); & wusa.exe /uninstall /KB:$sUpdate /quiet /norestart; Wait-Process wusa; Start-Sleep -s 1 }```
- C:Windows/servicing/Packages...edit mum files to force remove updates
  - ```$mumFiles = Get-ChildItem . *.mum -rec```
  -```foreach ($file in mumFiles){(Get-Content $file.PSPath) | Foreach-Object { $_ -replace "permanent", "removable"} | Set-Content $file.PSPath}```


## Python
### Server
- ```python -m SimpleHTTPServer 8000```
- ```python3 -m http.server```
