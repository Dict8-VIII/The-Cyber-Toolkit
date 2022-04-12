#!/usr/bin/env python
# coding: utf-8

# # Killchain - Info Gathering
# 
# The first step in the Killchain process is Information Gathering. This centres around investigating a target using publicly available data. As a rule of thumb, if you're accessing the target then your in the next step already. Gathering data without hitting the target is also known as "Passive" reconnaissance.<br>
# Why do we need to do reconnaissance? 
# - We need to know our target
# - Publicly available data can be used for some attacks
# - Hidden endpoints arent so hidden
# - Old information can be valuable
# 
# So, what can we do without hitting the target? Well a lot actually.
# 
# ## Dorking (Google)
# How's your google-fu? Google is a great source for public data and it's free. What more could you want? Theres a few options with Dorking
# 
# - site:*.domain - This will return all sites Google's spider has with the domain. Pairing this with "password" could possibly return password files on the site. Remember if you then connect to the site to retrieve the file/page, then you are now in "active" recon.
# 
# - Searching for Job applications. These tend to include the infrastructure the site runs on (i.e. Must have excellent knowledge in Windows SERVER 2019 and PHP).
# 
# ## Favicon
# This is a weird one, the little icon on the site's URL can also be used to determine the OS running behind the server. This is ACTIVE.
# 
# ## crt.sh (cert domain history)
# 
# ## DNS Recon
# 
# ## Sublist3r
# 
# ## FFuf??
# 
# ## WhoIs
# WHOIS is a RFC3912 request to a nameserver (Port43) that can be used to determine information about the domain name including who it was registered to, when it was registered and the contact details of the registration. You can also see who hosts the nameserver. This can be used for some social engineering attacks or understanding possible WAFs. For Linux, this is a built in command:
# > WHOIS google.com
# 
# ## NS Lookup
# nslookup (or name server lookup) queries a domain for its name servers (DNS). It can be used to query the site's DNS server for possible records. While this is considered passive, I'd list this in the ACTIVE group of commands. The basic format is:
# >nslookup [options] [domain.com]
# 
# The options are:
# - TYPE=A: IPv4 Addresses
# - TYPE=AAAA: IPv6 Addresses
# - TYPE=CNAME: Canonical Name
# - TYPE=MX: Mail Exchange
# - TYPE=SOA: Start of Authority
# - TYPE=TXT: TXT records... gasp!
# 
# ## dig
# DIG is basically the same as NSLOOKUP, but returns some more data. The format is 
# 
# > dig [options] [domain] [type]
# 
# Options are:
# - @10.10.10.10 : Ask 10.10.10.10 for the records
# 
# Types are the same as NSLookup, the DNS record types.
# 
# ## DNSDumpster
# [DNSDumpster](https://dnsdumpster.com/) is a website that combines all of the above DNS queries, and also puts them in easy to read formats tables and graphs. It can be used to discover extra subdomains and tries to resolve all names, IPs and even geo location. It looks quite helpful...
# 
# ## Shodan.io
# A great website for analysing a target. Shodan builds a collection of device properties in the same way that a search engine builds a collection of pages. It pulls data such as:
# - Server Builds & Versions
# - Server Ports
# - GeoLocation
# - Hardware Type
# 
# ## Social Media
# Facebook, Linked in, Job searches etc

# In[ ]:




