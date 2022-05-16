#!/usr/bin/env python
# coding: utf-8

# # Metasploit Framework
# 
# The MetaSploitFramework (msf / Metasploit) is a collection of exploits, payloads, scripts, enum tools,  has its own custom shell, nmap and will probably even walk the dog if you asked nicely enough. <br>
# This page is centred around the free version, which is terminal only.
# 
# ## Components
# 
# ### msfconsole
# This is the terminal interface for the free version of metasploit. It also installs a postgresSQL instance, where it stores your history, which must also be running when you launch it.
# 
# ### Modules
# The componets of Metasploit that can be used for a wide variety of tasks. These are further grouped by the purpose, and these can be listed. They are found in
# 
# > opt/metasploit-framework-5101/modules/
# 
# 1. Exploits
# 2. Scanners
# 3. Payload
#     - Singles: Self contained payloads that run 'standalone'
#     - Stagers: An initial connection channel is created using an exploit and small payload. It then 'calls' stages.
#     - Stages: larger payloads used by a stager.
#     - Singles tend to be in a 'higher' level and further data is _ separated. Stagers are / separated.
#     1. generic/shell_reverse_tcp -> Single
#     2. windows/x64/shell/reverse_tcp -> Stage
# 4. Auxillary
# 5. Encoders: Encodes a payload to evade signature-based AV
# 6. Evasion: More active methods to evade AV
# 7. Post
# 
# 
# ### Tools
# There are a few built in tools for metasploit. The biggest of these is MSFVenom. This is covered in [another page](Msfvenom.ipynb)
# 
# 
# <hr>

# ## The Basics
# 
# ### Launching
# 
# If you need to start the postgress instance manually
# 
# > sudo service start postgressql
# 
# Launching the Console
# 
# > msfconsole
# 
# <hr>
# 
# 

# ## Functional Commands
# 
# SET, OPTIONS, EXPLOIT, SEARCH
# SETG, clearG, BACK, USE
# 
# 
# ### Simple Example
# 
# search for an exploit (includes scanning and post exploit 'exploits')
# 
# > search Eternal_Blue <br>
# > search CVE-2017-0144 <br>
# > select # (your number from the list)
# 
# determine which paramaters need to be set
# 
# > options
# 
# Set the paramaters' value (this includes the default payload as described)
# 
# > set Lhost 127.0.0.1 <br>
# > set Rhosts 127.0.0.2 <br>
# 
# <hr>

# ## Working with databases
# 
# In the 'real world' we arent just attacking a single target, but a whole scope of targets. To facilitate this, metasploit has the option to create DB workspaces to separate scope. <br>
# 
# To use this feature, you must start the SQL server using
# 
# > systemctl start posstgresql
# 
# And then initialise the DB using
# 
# > msfdb init
# 
# You can then start the metasploit framework (msfconsole) and check the db is running with
# 
# > db_status
# 
# 
# ### Workspaces
# A workspace is an 'environment' where tasks can be run. This is similar to an env (in python) where the tasks are in a separate enviroment to other workspaces. Isolated isnt quite the right word, but it gives a good impression.
# 
# - Running the command workspace gives your current workspace
# - workspace -a [name] creates a new workspace
# - workspace -d [name] deletes the workspace
# - workspace [name] swaps to the workspace ("default" is default)
# - workspace -h lists the help
# 
# ## DB Functions
# Some metasploit functions also have db equivalent functions. These write the data to the db as well as the terminal.
# 
# ### db_nmap example
# 
# You can run an nmap scan using
# 
# > db_nmap [arguements]
# 
# This will then write the results to the db. These can be queried with either
# 
# > hosts <br>
# 
# OR
# 
# > services<br>
# > services -S 'value' searches the services for a name
# 
# <hr>
# 
# ### Eternal Blue example
# 
# 1. Scan for machines using db_nmap
# 2. Use auxiliary/scanner/smb/smb_ms17_010
# 3. Set the hosts using "hosts -R" to populate the RHOSTS variable
# 4. run the exploit with "exploit" or "run"
# 
# This will then run the scan against all recorded IPs and return those which may be vulnerable.
# 
# <hr>

# ## Sessions
# Sessions are 'open connections' which tend to be created after a successful exploit.
# 
# - bg: background the current session
# - sessions [i]: swap to session 1
# - sessions: list all current sessions
# 
# <hr>

# ## Meterpreter Shell
# 
# - help : uhh....
# 
# <br>
# 
# - ps : List processes
# - migrate : Migrate to another process
# - search : Search for a file "search -f name.ext"
# - bg : stores as a sessions
# - load : loads a meterpreter extension
# - run : runs the extensions
# - sessions : swap session within session... sessionception....
# - shell : creates a shell, exiting it returns to the session
# 
# <br>
# 
# - screenshare : watch the remote screen
# - webcam_chat/list/snap/stream : do the webcam things
# - getsystem : attempt to get "local system" rights
# - hashdump : dumps the (windows) hashes
# - sysinfo : name, build, domain etc
# 
# <hr>

# ## Fun exploits
# 
# ### Eternal Blue
# This one is easy, if youre running windows 7 and have SMB enabled (spoiler, they all do), you're screwed
# > search Eternal_Blue
# 
# ### Hashdump
# Dumps all the hashes in an exploited windows box, stores in Metasploit DB.
# > search post/windows/gather/hashdump
# 
# ### Crack Windows
# Follows on from the above hashdump, try to crack the passwords we have... borrowed...
# If its a good password, this is gonna take a while.... use John instead
# > auxiliary/analyze/crack_windows
# 
# ### Escalation Suggester
# One of the built in tools for PrivEx. Requires a session to be created already. I havent had much luck with this though
# > multi/recon/local_exploit_suggester
# 
# <hr>
