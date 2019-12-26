$confirmation = Read-Host "Is everything saved/closed?"
if ($confirmation -eq 'y') {
    if (($($(bcdedit | select-string hypervisorlaunchtype) -split '\s+')[1]) -eq "Off") {
        Write-Host "Enabling Hyper-V"
        bcdedit /set hypervisorlaunchtype auto
        Restart-Computer
    }
    else {
        Write-Host "Disabling Hyper-V"
        bcdedit /set hypervisorlaunchtype off
        Restart-Computer
    }
}
else {
    Write-Host "Save everything then run this again as admin"
}
