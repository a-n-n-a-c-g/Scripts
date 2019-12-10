$d = Get-Date -Format FileDate

$filename1 = $d + "00.txt"
$filename1 
Get-ChildItem -Attributes Hidden -R > $filename1

Start-Sleep -Seconds 10
$filename2 = $d + "01.txt"
$filename2 
Get-ChildItem -Attributes Hidden -R > $filename2

$diff = compare-object (get-content $filename1) (get-content $filename2)
$diff

$diff | Add-Content diff.txt
