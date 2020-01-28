# This detects hidden files in the tmp folder.
# A quieter way of accomplishing this exploit is to set the file with both the hidden and system attributes.
# attrib +s +h "<filepath>" ....... sets a file as a system file
# attrib -s -h "<filepath>" ....... sets a file back to a normal file

$mypath = "C:\Users\Adminsitrator\tmp"
Set-Location -Path $mypath
$newscan = Get-ChildItem -Attributes Hidden -R -Path $mypath #new scan results into var
if(Test-Path -Path "expected.xml") {
    $expected = Import-Clixml -Path "expected.xml" #read this in as var
    $var1 = Compare-Object -ReferenceObject $expected -DifferenceObject  $newscan -Property Name, Mode
    [string]$var1 >> diff.txt
    }
$newscan | Export-Clixml -Path "expected.xml" #overwrite expected
