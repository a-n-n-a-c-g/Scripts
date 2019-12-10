$confirmation = Read-Host "Is everything saved/closed?"
if ($confirmation -eq 'y') {
    if (((Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All).State) -eq "Disabled") {
        Write-Host "Enabling Hyper-V"
        echo y | powershell Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All
    }
    else {
        Write-Host "Disabling Hyper-V. For who knows what reason you're gonna have to restart again after this boots up. I am sorry."
        echo y | powershell Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All
    }
}
else {
    Write-Host "Save everything then run this again as admin"
}
