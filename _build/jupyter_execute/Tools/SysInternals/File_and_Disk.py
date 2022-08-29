#!/usr/bin/env python
# coding: utf-8

# # File and Disk Tools
# 
# 
# <hr>

# ## Sigcheck
# Sigcheck is a tol for checking file details, this includes
# - version
# - status
# - timestamps
# - signature details & cert chains (I didnt know files had cert chains)
# 
# It can also check the file against 'over 40 antivirus engines' and can upload a file to be scanned.
# 
# ## Arguements
# Standard Use (gives help)
# > sigcheck -accepteula
# 
# - -u: show files unknown to AV (virus total) or have no signature
# - -e: scan executable files only (not extension based)
# 
# As you can guess, you can define a directory to scan
# 
# > sigcheck -u -e c:\windows\system32 -accepteula
# 
# <hr>

# ## Streams
# Streams are file contents stored under the same 'file'. Its a property of NTFS (so mainly Windows). Under the same file, you can multipel contents or attributes which arent visible under normal operation. ADS, or Alternate Data Streams are those outside the default $DATA stream
# 
# ## Arguements
# Standard Use
# > streams -accepteula
# 
# Streams are properties of files, not directories. You can provide a file or directory however.
# > streams C:\Users\Admin\Desktop\files.txt
# 
# ![SysInternals_StreamsExample.png](../../images/Tools/SysInternals/SysInternals_StreamsExample.png)
# 
# To view or open an ADS, it must be passed as an arguement
# > streams C:\Users\Admin\Desktop\files.txt:$ADSName
# 
# ![SysInternals_StreamsView.png](../../images/Tools/SysInternals/SysInternals_StreamsView.png)
# 
# <hr>

# ## Sdelete
# Sdelete impliments the DOD 5220.22-M wipe method. Basically its a government standard for how to clear a file from disk completely. Do do this it
# 
# - Writes 0s to the drive and verifies
# - Writes 1s to the drive and verifies
# - Writes a random value to the drive and verifies
# 
# ### Arguements
# 
# - -p Number of passes to run (default 1)
# - -c Cleans a disk (must have 0 volumes)
# - -r Removes 'read only' attribute
# - -z Zeros free space (guess thats good for thin VMs)
# - -s Recursive subdirectories, careful with this one.
# 
# Delete a file
# > sdelete -p 1 [file]
# 
# Clear a drive
# > sdelete -p 1 -z|-c [disk number]
# 
# <hr>
