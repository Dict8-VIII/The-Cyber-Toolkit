#!/usr/bin/env python
# coding: utf-8

# # File Downloader
# 
# ## V1.0
# This is actually a uni assignment that I finished at 2.0. Renamed as 1.0

# In[1]:


'''
This python script opens a file named urls.txt in the  current folder and
downloads each url sequentually. Downloaded files are saved into the current folder.

Requirements
* In urls.txt URLs must be one per line and no line can be blank
* The URL must not use GET parameters (e.g. http://server/retrieve?file=myfile)
* urls.txt must be stored in the same folder as this file
* You must have read and write permission to this folder

v2.0 : 04/06/22
Additional function to allow selection of file save location
'''

import os
import urllib.request

#Links moved above the chdir, to ensure it can be in the current location
#Could just add it to the path...
links = open('urls.txt', 'r')

# Addition of where to save the file(s)
save_location = input("Hello. Where would you like to store the files [leave empty for current directory]:")
if (save_location == ""):
    save_location = os.getcwd()
    
os.chdir(save_location)

for link in links:

    #Get one line of text (e.g. http://server/files/grades.doc),
    # then get the filename from the end of the URL
    link = link.strip()
    filename = link.rsplit('/', 1)[-1]

    #Does this file exist in this folder? If not, download it
    if not (os.path.isfile(filename)):
        #print('Downloading: ' + filename )
        print("Downloading", link, "and saving as", save_location+filename)
        try:
            urllib.request.urlretrieve(link, filename)
            print("File size was", os.path.getsize(filename))
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')
    
    #File exists; don't download
    else:
        print("This file exists already.")

#End of program
print("Finished downloading.")


# V2.0

# In[3]:


'''
This python script opens a file named urls.txt in the  current folder and
downloads each url sequentually. Downloaded files are saved into the current folder.

Requirements
* In urls.txt URLs must be one per line and no line can be blank
* The URL must not use GET parameters (e.g. http://server/retrieve?file=myfile)
* urls.txt must be stored in the same folder as this file
* You must have read and write permission to this folder

v2.0 : 04/06/22
Additional function to allow selection of file save location
'''

import os
import urllib.request

#Links moved above the chdir, to ensure it can be in the current location
#Could just add it to the path...
#links = open('urls.txt', 'r')

# Addition of where to save the file(s)
save_location = input("Hello. Where would you like to store the files [leave empty for current directory]:")
if (save_location == ""):
    save_location = os.getcwd()
    
os.chdir(save_location)

arguements_list=('Darebin', 'Hume')

for arguement in arguements_list:
    target = "https://victorianwomenshealthatlas.net.au/reports/factsheets/Sexual%20and%20Reproductive%20Health/" + arguement + "/VWHAtlas%20Fact%20Sheet%20Sexual%20and%20Reproductive%20Health%20" + arguement + ".pdf"
    
    #link = link.strip()
    filename = target.rsplit('/', 1)[-1]
    print("Target: ", target)
    print("File: ", filename)



    #Does this file exist in this folder? If not, download it
    if not (os.path.isfile(filename)):
        #print('Downloading: ' + filename )
        print("Downloading", target, "and saving as", save_location+filename)
        try:
            urllib.request.urlretrieve(target, filename)
            print("File size was", os.path.getsize(filename))
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')
    
    #File exists; don't download
    else:
        print("This file exists already.")

#End of program
print("Finished downloading.")


# In[ ]:




