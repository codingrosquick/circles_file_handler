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

from utils import ipwd, ils, icd, init_cache, remove_file_from_cache, create_irods_env
from global_variables import local_folder, cyverse_path_server_resources


# ======================= FILESHARE COMMANDS =======================
'''
These commands allows to perform remotely bash navigation commands within IRODS files.
'''

print('\n------------------------IRODS CONFIGURATION------------------------\n')

print('Going to /iplant/noecarras/resources_file_iterator/ with the irods cd command')
icd(cyverse_path_server_resources)

print('\nRetrieving the current location on CyVerse with the irods pwd command')
location = ipwd()
print('We are located at:\t', location)

print('\nRetrieving the folder structure at our current location with the irods ls command')
folder_structure = ils()
print('The folder structure at our current location is:\t', folder_structure)

# ======================= I/O COMMANDS =======================



# ======================= CACHE COMMANDS =======================



