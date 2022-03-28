#!/usr/bin/env python
# coding: utf-8

# # Powerup
# 
# A powershell script to attempt privelige escalation on a windows machine. It can be sourced from:
# > https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1
# 
# Once coppied to the target machine, it must be invoked using 2 commands
# 1. ./powerup.ps1
# 2. Invoke-AllChecks
# 
# The first command launches the script (when running from meterpreter in kali), then we run 'all checks' to see what we can find :-) <br>
# NOTE: powershell requires '\\' as '\' in meterpreter (must escape the escape char)
# 
# 
# 
