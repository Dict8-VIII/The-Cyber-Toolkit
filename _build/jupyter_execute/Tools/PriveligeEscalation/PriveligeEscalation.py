#!/usr/bin/env python
# coding: utf-8

# # Privelige Escalation
# 
# There are any number of exploits that can get you access to a machine (and ideally a shell), but if a developer is even semi-competent, the service will only be running as a low privelige user. For full pwn-age however, a local root, local admin or Domain Admin are the real prizes. At the end of the day, privelige escalation is like giving yourself a promotion.
# ![PrivEsc-self_promotions.jpg](../../images/PrivEsc-self_promotions.jpg)
# 
# Note: Privelige escalation isnt a purely remote situation. It is also an internal threat, whereas an employee may want to gain access to information they arent supposed to have (a helpdesk operator shouldn have access to finance details however, but a domain admin could probably get to it).
# 
# There are 2 forms of privelige escalation, vertical and horizontal. A vertical escalation is moving to more rights (user -> admin for example), while a horizontal escalation is to move to the same level (we're both in helpdesk, but they have passwords saved on their desktop). Most of the time our goal is vertical movement, but horizonal movement may help get us there.
# 
# ## Trivial Checks
# There are some checks that can be done easily. The first is linux specific.
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

# In[ ]:




