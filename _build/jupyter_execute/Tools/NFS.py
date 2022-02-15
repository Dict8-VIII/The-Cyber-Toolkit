#!/usr/bin/env python
# coding: utf-8

# # NFS
# 
# Network file shares (NFS) are a key component of modern enviroments. Files need to be shared, resources accessed and memes reposted. OK, maybe that last one isnt a key part, but you get the point.
# 
# ## Accessing a Share from a Linux Box
# 
# First, you need to create a directory where the NFS will be mounted locally
# 
# > mkdir /tmp/mount
# 
# Next, mount the remote directory at this location
# 
# > sudo mount -f nfs \[IP]:\[Share] /tmp/mount -nolock
# 
# ### Samba
# 

# In[ ]:




