'''
--------------------------------------------------------------
                    IRODS and CyVerse I/O
--------------------------------------------------------------
This example file shows some capabilities given by this utility class.
Here, we discuss the available wrapper on IRODS commands.
It allows to perform and automate actions on CyVerse's file storage system.

NOTE: Be sure to have configured your cache and your irods environment before 
testing these functionnalities. You can do so by using the file 'example_configuration.py'

Resources for more information:
- IRODS: https://docs.irods.org/4.2.11/
- python-irodsclient: https://github.com/irods/python-irodsclient
- CyVerse: https://cyverse.org/discovery-environment
--------------------------------------------------------------
'''

import asyncio
from datetime import datetime
from fileinput import filename
import os
from utils import ipwd, ils, icd, init_cache, remove_file_from_cache, create_irods_env, IRODSGet, IRODSPut, getIRODSSession
from global_variables import cyverse_path_server_resources, local_temp_folder, cyverse_path_server_resources_test


# ======================= FILESHARE COMMANDS =======================
'''
These commands allows to perform remotely unix navigation commands within IRODS files.
'''

# print('\n------------------------IRODS COMMANDS------------------------\n')

# print('Going to /iplant/noecarras/resources_file_iterator/ with the irods cd command')
# icd(cyverse_path_server_resources)

# print('\nRetrieving the current location on CyVerse with the irods pwd command')
# location = ipwd()
# print('We are located at:\t', location)

# print('\nRetrieving the folder structure at our current location with the irods ls command')
# folder_structure = ils()
# print('The folder structure at our current location is:\t', folder_structure)


# ======================= I/O COMMANDS =======================
print('\n------------------------I/O COMMANDS------------------------\n')
file_to_download = '/iplant/home/noecarras/resources_file_iterator/default/file_exploration&full_exploration_publishable_circles&create_on=2021-12-01_06:10:16.920970&root=_iplant_home_sprinkjm_publishable-circles.csv'

# NOTE: we have to create an async loop and wait for its completion to be able to perform
# an 'await' in the python script. See the link below for more information:
# https://stackabuse.com/python-async-await-tutorial/, section 'Running the Event Loop'

def run_async_func(async_func):
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(async_func)
    loop.close()
    return res

# print(f'Downloading this file: {file_to_download} to the local temp folder.')
# local_path = run_async_func(IRODSGet(file_to_download, local_temp_folder))
# print(f'The file has been downloaded into: {local_path}')
local_path = '/Users/noecarras/Documents/03_Berkeley_EECS/cours/Capstone_RL_validation/filehandler/circles_file_handler/temp_cache/file_exploration&full_exploration_publishable_circles&create_on=2021-12-01_06:10:16.920970&root=_iplant_home_sprinkjm_publishable-circles.csv'

dl_filename = os.path.basename(local_path)
print('dl: ', dl_filename)
new_filename = dl_filename[:-4] + '&d' + str(datetime.now()).replace(' ', '') + '.csv'
print('upl; ', new_filename)

remote_upload_path = os.path.join(cyverse_path_server_resources_test, new_filename)
print(f'Uploading this file: {local_path} to the remote test folder: {remote_upload_path}')
remote_path = run_async_func(IRODSPut(remote_upload_path, local_path))
print(f'The file has been downloaded into: {local_path}')


# ======================= CACHE COMMANDS =======================
print('\n------------------------CACHE COMMANDS------------------------\n')

# list the files in cache

# remove 1 file

# init cache


# ======================= MANIPULATING IRODS SESSIONS =======================
'''
I/O Commands are performed using python-irodsclient.
To handle the requests for uploading and downloading, it uses Sessions.

Below is an example or creating a long lasting session and uploading a file with this.
It can be useful for instance to upload large files.
'''

print('\n------------------------MANIPULATING IRODS SESSIONS------------------------\n')

# Create a session


# Use it to download a file

