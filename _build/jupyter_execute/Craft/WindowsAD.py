#!/usr/bin/env python
# coding: utf-8

# # Windows Active Directory
# 
# The Windows Active Directory, or AD, is a service that manages authentication in a domain. This page focuses on what and AD is, and how it works. If you're more interested in attacking AD, check out the [Kerberos](Kerberos.ipynb) page for understanding or some of the tools such as [kerbrute](../Tools/Kerbrute.ipynb).<br>
# A good chunk of this content is adapted from https://tryhackme.com/room/winadbasics
# 
# ## The Basics
# So, what is an AD and why do we need one? Think about your situation at home. You might have a few laptops/windows tablets, maybe a couple of desktops. These probably all have their own logins and any network shares are probably open internally; no reason to hide the media server. This probably works quite well. Its a bit of work to set these up if you get a new device, but its not the end of the world. If someone needs to borrow another computer, you might just leave it logged in for them or create their own account<br>
# Now imagine you suddenly had 300 teenagers added to the house, and they all brought along their own laptops. Some wanted so share a media server, others had special photos to back up, the girls made a 'girls club' that they boys arent allowed in, and we want everyones' internet access to stop at midnight. Also you need to have a login for all these devices because people keep forgetting their passwords. You could manually set these all up, one by one, but theres a few problems here<br>
# 
# - It will just take a long time<br>
# - The chances are, you'll get something wrong<br>
# - What if the media server password changes or you buy a new one? Are you going to update all 300 devices<br>
# - What if someone buys a new laptop, are you going to go through every device and change it?<br>
# - Its exam time, and you want to allow internet access later but only for research and not 'research purposes'.<br>
# - What if they want to share devices, but only to browse the internet and not change things?<br>
# 
# As you may be thinking, this is going to take a while. What if we could change settings on a group of devices, instead of every device itself? Enter Active Directory & Domains. The general way to achieve this is<br>
# 
# 1. Create a Domain Controller to host the domain. A domain is known by its name,normally in the format something.something, such as WhoAreYouPeople.local<br>
#    - A Domain Controller hosts the Active Directory Domain Service (AD DS), which is a catalogue of data which can be read by devices on the domain. The share is known as the SYSVOL.
# 2. Create groups in the domain, known as organisational units (OUs).<br>
#    -  These can then be further divided into sub groups<br>
#    -  A sub group inherets from its upper groups<br>
#    -  You can only be a member of one group by type (user or computer)<br>
# 3. Create rules to apply to these groups, or subgroups. As above, subgroups inheret from upper groups<br>
# 4. Create users in the domain, and assign each to a group<br>
# 5. Join computers to the domain, and then assign each to a group<br>
# 
# If you do all of this correctly, you can now assign rights and rules to each group, assign tasks and access rights and accounts can be used between devices without creating a logon stored on each. Nice
# <br>
# <hr>
# 

# ## Managing an AD - Types
# 
# There are a few types in a domain, some of which we have already covered. It is important to understand the distinction between these as there are certain tasks that can only be performed on some groups. It also helps when you need to talk to someone else and sound like you know what youre doing....
# 
# ### Users
# Depending on what your domain looks like, this will probably be the largest 'type' in your domain. Users are also called Security Principles. This is because they are assigned rights over other resources.<br>
# The most common type of user will be a person, John/Jane/Jordan/Janet etc... This isnt the only type of user however. A service (such as SQL server) is normally run as a 'user' type. Why? So you can assign rights to them as well. Think back to the example of the media server. Perhaps you have a service that downloads media art and subtitles for your movies. The service still needs to authenticate with the media server before it can make changes to a file. Services are people too... <br>
# 
# 
# ### Machines
# Also called devices. It may sound odd that devices have a login to the domain, but after a while you should realise it just makes sense. The machine account doesnt have much rights in the domain, but it is usually a local admin on 'itself'. They can be easily identified as they end with a '&#36;'. So the laptop "HomePC" will have the machine account "HomePC&#36;".<br>
# 
# The password for a machine account is changed automatically and has length 120, made of random characters.<br>
# 
# 
# ### Security Groups
# This should be quite easy. There are groups in the domain which can make it easier to assign rules to groups of accounts instead of individual ones. They can be a mix of account types, as well as other groups. A full list can be found in the [Microsoft Docos.](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups)
# 
# - Domain Admins: Admins for the domain, thats easy huh. They can (by default) administer everything on the domain, including DCs<br>
# - Server Operators: Accounts that can make changes on a DC, they cant change who has admin group roles however<br>
# - Backup Operators: Can access files, ignoring their permissions. It's for backup but can guess why this could be fun for a red team<br>
# - Account Operators: Can modify other accounts in the domain<br>
# - Domain Users: All users in the domain<br>
# - Domain Computers: All the machine accounts in the domain<br>
# - Domain Controllers: The DCs in the domain<br>
# 
# 
# ### Organisational Units (OUs)
# And OU is like a 'folder' in the domain, where a user or machine 'sits'. You can also have an OU within another OU, and they do inherit from their parents. We'll get to this a bit more when we look at a domain structure. A user or machine can only be in ONE OU at a time.<br>
# 
# An OU and Security Group may sound similar, but they have very different usage. A key point is that an entitiy can only be a member of one OU, but can be in multiple Security Groups. An OU is used for logical groups which may have different policies, for a businsess this could be different departments. A security groups is to give rights / permissions to a resource, such as a shared resource.
# 
# <hr>

# ## AD Structure
# 
# --- Working on this ---
# 
# <hr>

# ## Managing Computers
# 
# If a machine joins the domain with the GUI (or without specifiying an OU path in the Domain Join), it will get dropped in the "Computers" OU. This is nice, but if we have a full domain setup we will likely need to move this to a location that will apply the correct GPOs. Whats a GPO? Well its a group policy. If that doesnt help, check the next section....
# 
# <hr>

# ### Group Policy Objects (GPOs)
# 
# A GPO is a 'rule' that is applied to an OU.
# 
# <hr>
