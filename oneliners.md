# Helpful one-liners
## Bash
### File Manipulation
- Find lines in file2 that aren't in file1: ```comm -13 <(sort -u file1.txt) <(sort -u file2.txt)```
- Count number of unique lines in a file: ```sort hosts.txt | uniq -c | wc -l```
## Powershell
#### Firewall/Network
- ```new-netfirewallrule -DisplayName "Testing TCP/80" -Direction Inbound -LocalPort 80 -Protocol TCP -Action Allow ```
- ```remove-netfirewallrule -DisplayName "Testing TCP/80"```
- ```route add 192.168.0.0 MASK 255.255.0.0 192.168.230.1 METRIC 5```
- ```route delete 192.168.0.0 MASK 255.255.0.0 192.168.230.1 METRIC 5 ```

#### Scheduled tasks
- ```schtasks /create /tn myTask /tr "powershell -NoLogo -WindowStyle Hidden -file myScript.ps1" /sc minute /mo 1 /ru System ```
## Cmd
- Direct diagnostic tool for PC info: ```dxdiag```

## Python
### Server
- ```python -m SimpleHTTPServer 8000```
- ```python3 -m http.server```
