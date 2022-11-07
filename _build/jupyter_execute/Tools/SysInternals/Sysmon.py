#!/usr/bin/env python
# coding: utf-8

# # Sysmon
# 
# Sysmon is a part of the SysInternals package, and is an expanded version of the windows event logs. It provides more details and a more granluar control system. The Events within Sysmon are still stored in the event logs here:
# 
# > Applications and Services Logs/Microsoft/WIndows/Sysmon/Operational
# 
# Once Sysmon is installed, it persists through restarts and its primary purpose is to integrate with a SIEM system. Thats not to say you cant monitor it internally, its just where it can really shine. Sysmon itself can record multiple event types (29ish at the time of writing) and you can write either include or exclude rules to filter which events are captured. These rules are stored in the Sysmon config file. Filtering at the monitor can reduce the amount of analysis needed at the SIEM end, however if the rules are not well created it can also hide malicious activity. If starting out, its great to start with a template and configure for your environment (once you know what youre doing). THM recommended [this one by SwiftOnSecurity](https://github.com/SwiftOnSecurity/sysmon-config/blob/master/sysmonconfig-export.xml).
# 
# <hr>

# ## Config File
# 
# The config file is a .XML file. Within the XML is nested rules stored in groups, and each group is defined a matching type. The group then has its individual rules defined. The General structure is:
# 
# Sysmon Schemaversion
# - Some global rules
#   - Event Filtering
#     - RuleGroup name = "" groupRelation="or"
#       - ProcessCreate onmatch="exclude"
#         - rule 1
#         - rule 2
#         - rule 3
#       - /ProcessCreate
#     - /RuleGroup
# 
# 
# This is a very simple config file, which looks for the 'process created' event and excludes them from the logs. In this section we would have the 'trusted' applications, most likely the windows ones or BAU applications (such as chrome, office etc). Obviously some of these can still be malicious so should be carefully considered. In a 'full' config file, you would expect to have rules for all off the Event groups below.
#       
# <hr>

# ## Event Groups
# 
# As above, the config file can filter multiple event groups, but which should we be looking for?
# 
# ### 1: Process Creation
# As above, this event can be used to filter out 'safe' processes or include known 'bad' processes. Likely we would want to exclude known, not include what may be unknown. Part of excluding 'safe' processes is that we can also identify if a fake process is run by being mispelt or programs being launched from a non-standard location. Below we are excluding chrome and windows media player.

<RuleGroup name="" groupRelation="or>
  <ProcessCreate onmatch="exclude">
    <CommandLine condition="begin with">"C:\Program Files\Google\Chrome\Application\chrome.exe" --type=</CommandLine>
    <Image condition="is">C:\Program Files\Windows Media Player\wmpnscfg.exe</Image> 
  </ProcessCreate>
</RuleGroup>

# ### 3: Network Connection
# This time we are looking for an application making a network connection, or known malicious ports. When we're red teaming, this is part of why we dont use standard ports even on the red side, it's too easy to pick up.
<ruleGroup name="" groupRelation="or">
  <NetworkConnect onmatch="include">
    <Image condition="image">nmap.exe</Image>
    <DestinationPort name="Alert,Metasploit" condition="is">4444</DestinationPort>
  </NetworkConnect>
</RuleGroup>
# ### 7: Image Loaded
# It says image, but what it really means is a DLL being loaded by a process. As pretty much everything uses a .dll file. The below is an example of an "ImageLoaded" tag, but it also includes Image, SIgned and Signatures.
<RuleGroup name="" groupRelation="or">
  <imageLoad onmatch="include">
    <ImageLoaded condition="contains">\Temp\</ImageLoaded>
  </imageLoad>
</Rulegroup>
# ## 8: Remote Thread
# This event occurs when a process tries to inject code into another process. Theres 2 ways to approach this event below. The first is looking for a specific memory address ending, and the second is looking for processes that doent also have a parent process when this is done. There are legitimate times this event can be triggered, but these two options are pretty red flags.
<RuleGroup name="" groupRelation="or"?
  <CreateRemoteThread onmatch="include">
    <StartAddress name="Alert,Cobalt Strike" condition="end with">0B80</StartAddress>
    <SourceImage condition="contains">\</SourceImage>
  </CreateRemoteAddress>
</RuleGroup>
# ## 11: File Created
# 
# 
