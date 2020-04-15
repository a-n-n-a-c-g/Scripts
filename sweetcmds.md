# Helpful one-liners
## Bash
### File Manipulation
- Find lines in file2 that aren't in file1: ```comm -13 <(sort -u file1.txt) <(sort -u file2.txt)```
- Count number of unique lines in a file: ```sort hosts.txt | uniq -c | wc -l```
## Powershell
## Cmd
## Python
### Server
- python -m SimpleHTTPServer 8000
- python3 -m http.server
