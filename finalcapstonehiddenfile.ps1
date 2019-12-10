$mypath = "C:\Users\Adminsitrator\tmp"
Set-Location -Path $mypath
$newscan = Get-ChildItem -Attributes Hidden -R -Path $mypath #new scan results into var
if(Test-Path -Path "expected.xml") {
    $expected = Import-Clixml -Path "expected.xml" #read this in as var
    $var1 = Compare-Object -ReferenceObject $expeted -DifferenceObject  $newscan -Property Name, Mode
    [string]$var1 >> diff.txt
    }
$newscan | Export-Clixml -Path "expected.xml" #overwrite expected
