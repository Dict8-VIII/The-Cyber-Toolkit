#!/usr/bin/env python
# coding: utf-8

# # Kerberos Attacks
# 
# https://tryhackme.com/room/attackingkerberos
# 
# ## Commmon Terminology
# 
# - TGT: Ticket Granting Ticket. An Authentication ticket that requests service tickets from TGS for domain resources.
# 
# - KDC: Key Distribution Centre. A service for issuing TGTs and Service tickets. It has 2 components
#   - Authentication Service (AS)
#   - Ticket Granting Service (TGS)
#   
# - AS: Authentication Service. Issues TGT that are used by the TGS to request access to other machines and service tickets
# 
# - TGS: Ticket Granting Service. Tages a TGT and returns a ticket to a domain machine
# 
# - SPN: Service Principal Name. An identifier given to a service instance to associate it with a domain service account. Windows requires that services have a domain service account so a service needs an SPN set.
# 
# - KDC LT Key: KDC Long Term Secret Key. a KDC key is based on the KRBTGT service account. Used to encrypt the TGT and sign PAC.
# 
# - Client LT Key: Client Long Term Secret Key. The client key is basedo n the computer or service account. It checks the encryption of the timestamps and encrypts the session key.
# 
# - Service LT Key: The service key is based on the service account. It encrypts the service part of the service ticket and signs the PAC
# 
# - Session Key. Issued bythe KDC when a TGT is issued. It is provided to the KDC with the TGT when requesting a service ticket.
# 
# - PAC : Privelege Attribute Certificate.Holds all the users relevant information, it is sent with the TGT to the KDC to be signed by the Tartget LT Key and the KDC LT Key to validate the user.
# 
# ### AS-REQ w/ PRe-Authentication in Detail
# 
# 1. User requests TGT from KDC
# 2. User encrypts a timestamp NT hash and sends to the AS
# 3. KDC attempts to decrypt with users NT Hash
# 4. If successful, KDC issues a TGT and session key to the user
# 
# <hr>
# 
# ### TGT Contents
# The TGT itself comes from the user and is passed to the KDC. In return, if validated it returns a service ticket. <br>
# 
# It includes fields fields such as
# - Start/end/Renewal
# - Service Name
# - Target Name
# - Client name
# - Flags
# - Session Key
# - PAC
# 
# It is signed with the Service LT Key and KDC LT Key
# 
# <hr>
# 
# ### Service Ticket Contents
# A service ticket is split into 2 sections, the Service and User portion.<br>
# 
# Service Portion:
# - User Details
# - Session Key
# - It is encrypted with the service account NTLM hash
# 
# User Portion:
# - Validity Timestamp
# - Session Keys
# - It is encrypted with the TGT Session key.
# 
# <hr>
# 
# ### Authentication Overview
# The steps for Authenicating with Kerberos and the message types
# 
# 1. AS-REQ: The client requests an Authentication Ticket or TGT
# 2. AS-REP: The KDC verifies the client and returns an encrypted TGT
# 3. TGS-REQ: The client sents the encrypted TGT to the TGS with the SPN of the service where access is requested
# 4. TGS-REP: The KDC verifies the TGT and that the user has access, then returns a session key for the service
# 5. AP-REQ: The client requests the  service and sends the session key
# 6. AP-REP: The service provides access
# 
# <hr>
# 
# ### Kerberos Tickets Overview
# The tickets themselves dont have file extensions, but depending on your attacks these may be presented as files. A .kirbi is for Rubeus and .ccache for Impacket. They are usually base64 encoded and depending on the ticket can be used for a different attacks. A TGT must be used authenicated with the KDC to get service tickets, but this can return other details. More below.
# 
# <hr>
# 

# ## Attacks & Credentails Needed
# 
# No Domain Access
# - Kerbrute Enumeration
# 
# Access as any user
# - Kerberaosting
# - AS-REP Roasting
# 
# Access as a domain user
# - Pass the Ticket
# 
# Full domain (admin)
# - Golden Ticket
# - Skeleton Key
# 
# Service Hash
# - Silver Ticket
# 
# <hr>

# ## Rubeus
# 
# Check the tools section
# 
# <hr>

# ## Kerbrute Enumeration
# 
# Check the tools section for [Kerbrute](../Tools/Kerbrute.ipynb)
# 
# <hr>

# ## Kerberoasting
# Using either Rubeus or Impacket, you can dump the hashes for service accounts and then attempt to crack these in Hashcat. See the Rubeus or Impacket section for how to achieve this.
# 
# <hr>

# ## AS-REP Roasting
# Unlike kerberoasting, AS-REP Roasting can be used for any type of account. The only requirement is that the user has pre-authentication disabled.<br>
# See the Rubeus section for how to achieve this.
# 
# <hr>

# ## Pass The Ticket
# 
# Basically if you've logged into a machine and it hasnt rebooted, your ticket may be stored in memory. This can be dumped and used to impersonate your account without knowing your password.
# 
# This one is in MimiKatz. 
# 
# <hr>
