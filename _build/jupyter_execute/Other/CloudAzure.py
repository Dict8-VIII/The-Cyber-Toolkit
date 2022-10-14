#!/usr/bin/env python
# coding: utf-8

# # Cloud Providers - Azure
# 
# Azure Essentails
# From linked in course: Azure Administration Essential Training
# 
# portal.azure.com
# 
# 3 Types of cloud
# Public, private, Hybrid
# 
# Private - On Prem cloud
# - Portal based
# - Hides the infrastructure behind
# - Example: System Center2012 (microsoft)
# 
# Public Cloud - What we know as cloud
# - GCP, Azure, AWS etc
# - Pay based on usage
# - Reduces capital expenses, but increases operational expenses
# 
# 
# Hybrid
# - A mix of both
# - Private datacentre, with some in the cloud
# - Can be temp
# - Can be complex to manage
# 
# --
# 
# SaaS - Software
# PasS - Platform
# IaaS - Infrastructure
# 
# IaaS
# - You lease hardware (fundamentally)
# 
# PaaS
# - You lease servers
# - Web, SQL, Etc
# 
# SaaS
# - You lease Applications
# - Office365
# - Microsoft365
# 
# Can get blured
# - Services are more important now
# - Data Storage Services
# - Compute Services (both PaaS and SaaS)
# - Networking Services
# - Application Services (example AD)
# 
# --
# Azure subscription is independant of Office365
# each has their own portal
# One service can be shared, the users (can).
# Azure AD in Azure, Users in office365
# 
# Can have multiple subscriptions (like managing multiple clients). Under clients you can have the below
# 
# -----
# Services are 'components' that can be added
# There are extra portals to manage some services
# Resources are configured entities
# There is also a cloud shell, for cmd functions
# - Can be PS or BASH
# - PS can also be done from local with powershell modules
# 
# Resource Groups
# - Resources groups is top level (like a folder)
# - Can contain resources/services.
# - Can be managed as a group, started, stopped, managed etc
# - Can redeploy as groups as well (in another sub for example)
# - When you create a resource/service, you must apply to a Resource group
# 
# 
# Billing Accounts
# - Contains costs
# - Is based on resource groups
# - Analysis can predict monthly, as well as current (monthly)
# - Can show by resource as well
# - Can save views, then creates a link that can be used ot see the view
# - Budgets can be used to create alerts, but doesnt stop exceeding the budget
# -- can be used to notify of runaway costs etc
# 
# Security Center
# - Is a paid service
# - Audits the setup & includes recommendations
# - Compares to secuirty standards (number of passed tests)
# - Security Hygine, classes of issues
# - Can add local infrastructure as well
# - Can drill down by sub component
# - Can configure alerts
# 
# Storage Resources
# Includes datalake, AzureDataBox (upload from local)
# - Files is stored in StorageAccounts
# -- There are other options, but all must have this initially
# - NAME is global unique.. what? (because it becomes a web page)
# - Performance can be set
# - Can set replication rules, and how far it can be replicated
# - Can restrict by networks, including cloud vlan
# - Can tag (administratvie only)
# - WHen you dive into a resource, the groups on the left are 'blades'
# - Storage explorer can be used to see the contents
# - 4 Data types
# -- Blobs (Non structured)
# -- File shares (like shared storage)
# -- Queues 
# -- Tables (i.e. DB)
# - Can then create services on a type (containers)
# -- Give it a name, doesnt need to be global unique
# -- Can give policies on an individual instance
# - Data is encrypted automatically, uses azures, but can set own keys
# 
# 
# -----
# Powershell Cmdletts
# 
# Azure.microsoft.com
# - Under windows - Command line tools
# - PowerShell Windows intall - Azure powershell module
# - Can then run powershell modules
# -- connect-azurermaccount (promts for user/password)
# -- There are others, RM is resource manager
# -- get-azureRM{tab} gives all commands by tabs
# -- set-azureRM{name}
# -- help in front of everything gives help page
# 
# 
# -----
# Release Cycle
# 
# Private (like closed beta)
# Public (like open beta - says preview in services page)
# General Available
# (and classic, which is previous verisons, no resource groups)
# 
# Different SLA at each level. Preview has lower standards
# 
# ----
# Templates
# 
# 
