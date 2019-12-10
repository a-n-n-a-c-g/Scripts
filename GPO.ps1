Import-Module ActiveDirectory
Import-Module GroupPolicy

# Save GPO
Get-GPO -Name "Lab3" | Get-GPOReport -ReportType HTML -Path C:\Users\Administrator.4EYES\Documents\GPOReports1.html

# Pause for Key Press
Read-Host "Press Enter to Continue"

# Force GPO Refresh
gpupdate /force

#Display HTML Summary of differneces
Get-GPO -Name "Lab3" | Get-GPOReport -ReportType HTML -Path C:\Users\Administrator.4EYES\Documents\GPOReportsAll2.html

diff (cat C:\Users\Administrator.4EYES\Documents\GPOReports1.html)(cat C:\Users\Administrator.4EYES\Documents\GPOReportsAll2.html)  | Out-File -FilePath C:\Users\Administrator.4EYES\Documents\diff.txt

Rename-Item -Path "C:\Users\Administrator.4EYES\Documents\diff.txt" -NewName "C:\Users\Administrator.4EYES\Documents\diff.html" -Force

Invoke-Item C:\Users\Administrator.4EYES\Documents\diff.html
