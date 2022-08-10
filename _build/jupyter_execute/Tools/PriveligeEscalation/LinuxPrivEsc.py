#!/usr/bin/env python
# coding: utf-8

# # Linux Privelige Escalation

# ## Trivial Checks
# There are some checks that can be done easily. 
# 
# ### Sudo List
# The first is linux specific.
# 
# > sudo -l
# 
# While not an escalation itself, it lists what can be run as 'sudo' rights. Sudo is linux specific where a user can use admin priveliges for a task. This function lists what can be run as 'sudo'. An example would be /bin/su. If it is listed and you execute
# 
# > sudo /bin/su
# 
# then your terminal will suddenly have sudo rights. Obviously this is also one of the first things locked down in a system.
# 
# <hr>

# ## Users List
# A good check to run is to check the users list. On linux this can be done by printing the users file to the terminal:
# > cat /etc/passwd
# 
# The shadow file is also nice to have, it includes more things on the passwords but its only root readable & you need both to try cracking.
# > cat /etc/shadow
# 
# <hr>

# ## Linux User Rights
# All files (and folders) in linux have rights which can be represented by 3 digits. Each digit corresponds to an access group. <br>
# For the representation "123":
# 1. The 'user' who owns the file (the owner)
# 2. The 'group' who owns the file (
# 3. Everyone Else
# 
# Now, lets break down where the value of the position comes from. Keep in mind, this is how the value for each position is determined. There are 3 rights that can be assigned to each group; Read, Write and eXecute. Each of these rights is assigned a value (if permitted) and the sum of these values its the single digit of the group. For "all rights", the values are shown below. Note the order of groups and right is always the same.
# 
# >rwx <br>
# >421
# 
# Summing these gives the value for that group (with the max being 7). Relating this to the larger 3 groups, 700 would mean the owner has all rights to the file, and no-one else does. A few more examples are below for the full mapping:
# 
# >rwx-r..-r..<br>
# >421-4..-4..<br>
# >744
# 
# 744 means the owner has full rights, everyone else can only read
# 
# >rwx-r.x-r.x<br>
# >421-4.1-4.1<br>
# >755
# 
# 755 means the owner has full rights, others can only read and execute.
# 
# >rwx-...-...<br>
# >42.-...-...<br>
# >600
# 
# 600 means the owner can only read & write (but not execute), no-one else can do anything.
# 
# <hr>
# 
# ### Modifying Rights
# Its fairly easy to change the rights on a file, assuming you have the rights to do so
# 
# > chmod +x [file]
# 
# This adds execute rights to the user
# 
# > chmod 755 [file]
# 
# This adds 755 rights to the file
# 
# > chown [user] [file]
# 
# Changes the owner of a file from its current owner to the defined owner
# 
# <hr>
# 
# ### The SUID bit
# So, all the above makes sense (I hope). If not, read it again before this sections.<br>
# The SUID, or Set User ID is a special case in linux. When this is set, the file is executed with the 'current' user, but uses the rights of the owner. Unless you dive quite far into this, its probably easier to just think that the file is being run as the owner.
# 
# ![technicallycorrect.gif](../../images/technicallycorrect.gif)<br>
# Source: https://tenor.com/view/futurama-you-are-technically-correct-technically-correct-the-best-kind-of-correct-correct-gif-4979933
# 
# This may sound weird and insecure, but its actually a necessity for a number of tasks. For example, the average user cant modify the passwords file, but when they change their own password they need to. There is also a SGID bit, which is the same for groups. <br>
# 
# So, how is this represented? We've filled in all the spots in our permission set? Simply, we just steal the execute bit (in the owner for SUID, in the group for GUID).
# 
# So, if the SUID bit is set, 755 becomes
# 
# >rws-r.x-r.x<br>
# >421-4.1-4.1<br>
# >755
# 
# So the value doesnt change, just the representation. This is also where the case comes into play as well. All of the letter so far have been lower case, but its actually case sensitive. To quote [tbhaxor](https://tbhaxor.com/demystifying-suid-and-sgid-bits/):
# 
# <i>The translation would look like</i>
# 
# - <i>rwsrw-r-x – SUID bit set and the binary is executable</i>
# - <i>rwSrw-r-x – SUID bit set and the binary is not executable</i>
# - <i>rwxrwsr-x – SGID bit set and the binary is executable</i>
# - <i>rwxrwSr-x – SGID bit set and the binary is not executable</i>
# 
# <hr>
# 
# #### How to find files with SUID set
# 
# Great thing linux has a search function, huh?
# > find / -perm -u=s -type f 2>/dev/null
# - Find: What it says
# - /: whole directory
# - -perm -u=s: with permission SUID (-g=s for SGID)
# - -type f: of type file
# - 2>/dev/null: linux speak for "send errors to the null box" (ignore errors)
# 
# <hr>

# ## Capabilities
# Capabilities is a much more granular method of assigning rights to a program. Instead of giving a program root permissions, you give it specific tasks that it can run with higher priveliges. NOTE: These rights are given to the file, NOT to a user.
# 
# ### How to find files with capabilities
# 
# Very similar to the SUID search:
# 
# > getcap -r / 2>/dev/null
# 
# - getcap : Get Capabilities. It ignores files with none
# - -r : Search recursively
# - / : Search from root directory
# - 2>/dev/null : make the errors go away
# 
# <hr>

# ## Crontabs
# 
# Found in /var/spool/cron/crontabs, it is a txt file that linux uses similar to 'task scheduler' in windows.
# 
# <hr>

# ## Exploiting
# 
# So you've found a path that may lead to PrivEsc, great... now what? Unless you've found sudo rights on a shell, you'll probably need to leverage the path to turn it to an escalation.
# 
# ### GTFO Bins
# Enter [GTFOBins](https://gtfobins.github.io/gtfobins/nano/). This is a great page that includes so many ways to turn a path into an escalation. It includes
# - Sudo rights in a program to something leveragble
# - SUID rights in a program to something leveragble
# - Capabilities in a program to something leveragble
# 
# ### Exploting a Service - Linux
# Sometimes you may be able to create services to be executed as root (such as with cron). Write your script in a text file and save it as [name].service. The below steps will then register the service for you.
# 
# - systemd-analyze verify [name].service
# - systemctl link /xxx/yyy/[name].service (this must be an absolute path)
# - systemctl start [name].service
# 
# <hr>

# ## Tools To Add
# 
# - LES (Linux Exploit Suggester): https://github.com/mzet-/linux-exploit-suggester
# - Linux Smart Enumeration: https://github.com/diego-treitos/linux-smart-enumeration
# - Linux Priv Checker: https://github.com/linted/linuxprivchecker
# 
# <hr>
