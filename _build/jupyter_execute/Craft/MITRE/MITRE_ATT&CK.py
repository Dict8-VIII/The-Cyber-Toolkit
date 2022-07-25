#!/usr/bin/env python
# coding: utf-8

# # Mitre ATT&CK
# 
# ATT&CK, or Adversarial Tactics, Techniques and Common Knowlege is a framework of useful information about the landscape of cyber security. But what do these mean?
# 
# - Tactic : The goal or objective
# - Technique : How the objective is achieved
# - Procedure : How the technique is executed.
# 
# I'm still working on this myself, but an example would be getting data out of a database.
# 
# - Tactic : Retrieving a User List from the DB
# - Technique : SQL Injection
# - Procedure : Exploiting the login page to extract the DB via blind SQL injection.
# 
# The ATT&CK page can be found at [https://attack.mitre.org/](https://attack.mitre.org/). Overall it is a great resource for the Blue team, as well as a trove of information for the Red team
# 
# <hr>
# 

# ## Exploring the Framework
# 
# On first opening the URL, we are presented with the full framework which can be quite daunting at first<br>
# ![ATT&CK_Full_Framework.png](../../images/HackerCraft/MITRE/ATT&CK_Full_Framework.png)<br>
# 
# Breaking it down however, we can see the matrix is initially techniques split by the stage of an attack
# 
# - Reconnaissance
# - Resource Development
# - Initial Access
# - Execution
# - Persistence
# - Privilege Escalation
# - Defense Evasion
# - Credential Access
# - Discovery
# - Lateral Movement
# - Collection
# - Command & Control (C&C)
# - Exfiltration
# - Impact
# 
# Under "Privilege Escalation", for example, we can select the technique "Create or Modify System Process".
# 
# <hr>

# ## Data in a Technique
# 
# From here, we can now see what is provided for a single technique. We are given:
# - Rough Overview : A simple description
# - Procedure Examples : A time this has been used
# - Mitigations : Ways to reduce the impact if this technique is used
# - Detections : Ways to detect the technique
# 
# <hr>
