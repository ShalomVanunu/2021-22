from winreg import *

key = CreateKey(HKEY_CURRENT_USER,"Software\Policies\Microsoft\Windows\System")
SetValueEx(key,"DisableCMD",0,REG_DWORD,1)

#Hide clock
key = CreateKey(HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer")

SetValueEx(key,"HideClock",0,REG_DWORD,0)
