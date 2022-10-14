#!/usr/bin/env python
# coding: utf-8

# # Vulnerabilities
# 
# ## Common Terms
# 
# Threat : an entity which may wish to attack<br>
# Thread Actors : about the same<br>
# Threat Vector : the means of performing an attack<br>
# Vulnerability : A weakness in the system which an attacker could leverge to create a vector.<br>
# Asset : something that needs to be protected. Data, servers, switches, etc
# 
# <hr>
# 
# ## Risk
# Arranged by likelyhood against impact<br>
# 
# Risk Appetite/tolerance - How much risk a company can accept<br>
# 
# ## Types of Risk Treatments
# 
# ### Avoidance
# Elimination in OHS speak, removing the risk entirely
# 
# ### Mitigation
# Reducing the risk to a more acceptable level, such as by implimenting controls, admin, audits etc
# 
# ### Transfer
# Passing the risk to someone else, this could include a cloud provider (cloudflare) or Insurance (including cyber insurance)
# 
# ### Acceptance
# Make no changes, just accept the risk and monitor

# ## Access Control Concepts
# 
# Security control - a safeguard or measure designed to preserve the CIA triange.<br>
# 
# A physical control would be a seatbelt. An administrative control would be the law requiring its use.<br>
# 
# ### Access Controls
# 
# Subjects - The entity requesting access (user, endpoint, service, workstation, storage etc). This is the initiator and is active<br>
# Objects - The target of the access request (Server, Storage, workstation, Web Service etc). It is passive<br>
# Rules - The instruction that allows or denies access to an object by a subject.<br>
# 
# ### Defense in Depth
# A fundamental concept in all types of security. Defense in Depth is the concept that one defense can fail, so multiple layered defenses should be considered. These layers of security mean that if one line fails, there are still further defenses that are active. 
# 
# ### Principle of Least Privilege
# This one is common sense, but isnt always implimented well. Simply put, only access rights that are needed should be assigned. If someone wants to be able to read a file for their job, theres no reason to give them full rights to the whole storage; thats just unnecessary and means that a compormise of a 'limited' user gives far more access than is needed.
# 
# ### PAM - Privileged Access Management
# Sometimes users need a higher level of rights than their standard role. This could be to install software, access extra file locations or other privileged tasks. PAM is the concept of managing this 'higher level' to only be available when needed. For example, theres no reason for privileged access when reading your own emails, so why have it enabled?
# 
# ### Privileged Accounts
# A privliged account is one that has the higher level as a part of their standard role. For example, a Domain Admin or Helpdesk operation. As these accounts always have the higher rights, they should be managed much more strictly. This should likely include
# - 2FA / MFA
# - Additional Logging
# - If a user, more strict trust verification
# 
# 
