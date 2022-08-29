#!/usr/bin/env python
# coding: utf-8

# # OWASP Top 10 - 2021
# 
# From the Free Linked in course 2022.
# 
# ## 1 Broken Access Control
# 
# Being able to access areas you shouldnt be able to. Also includes data being sent to uninteneded recipients.
# 
# ## 2 Cryptographic Failures
# 
# Using non secure encryption. Also encryting at rest and in transit
# 
# ## 3 Injection
# 
# Not sanitising input, front end commands getting to the back end.
# An input is treated as a command
# 
# ## 4 Insecure Design
# 
# The Webapp not being secure by design. Storing passwords in plain txt, built on old infrastructure etc
# 
# ## 5 Digital Security Misconfiguration
# 
# Default settings, extra modules enabled etc
# Declining passwords (i.e. not enabling on device)
# 
# ## 6 Vulnerable and outdated components
# 
# Old versions running, unpatched etc.
# 
# ## 7 Identification and Authentication Failures
# 
# Doesnt ask for authentication, verifying ID, outdated certs etc. Sessions not being closed out (someone else user being available).
# 
# ## 8 Software and Data Integrity Failures
# 
# Updates not verified (by update internally). Agile may introduce concerns. Plugins, repos, 3rd party software etc. Focused around rapid development. A subset of 6
# 
# ## 9 Security Logging and Monitoring Failures
# 
# Lack of logging, fundamentally is that they will happen. Monitoring should be able to identify its in progress and this can be managed. Opportunities should be leveraged to stop an attack.
# 
# ## 10 SSRF - Server Side Request Forgery
# 
# Send requests while pretending to be someone else?
# Internal API calls.
# Server requesting info from another location.
# Managed by permit/deny lists. Limit connections by expected traffic
# Allow - External
# Deny - Interal where it shouldnt be looking
# 
