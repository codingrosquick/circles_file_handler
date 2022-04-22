'''
--------------------------------------------------------------
                    IRODS and CyVerse I/O
--------------------------------------------------------------
This example file shows how to configure this package.
It shows how to confiugure the cache and the irods envrionment.

To do this configuration, perform the following steps:
    1. Open /utils/global_variables.py, then set the variable local_path
        to the root of the folder you will be working into.
    2. Set your CyVerse username in the username variable below
    3. Set skip_config_irods and skip_config_cache to False
    4. Run the file
    5. Set skip_config_irods and skip_config_cache to True to avoid
        erasing your configuration

Resources for more information:
- IRODS: https://docs.irods.org/4.2.11/
- python-irodsclient: https://github.com/irods/python-irodsclient
--------------------------------------------------------------
'''

# IMPORTS

import subprocess
from utils import ipwd, ils, icd, init_cache, remove_file_from_cache, create_irods_env, local_folder


# VARIABLES FOR THE TEST
# Set both variables to true to do the configuration properly.

# Set to true to skip the irods environment configuration
skip_config_irods = True

# Set to true to skip the cache folders configuration
skip_config_cache = True


if __name__ == '__main__':

    # ======================= IRODS CONFIGURATION =======================
    '''
    To connect to CyVerse, you need your profile to be set.To retrieve this profile, the irods client tries:
        1. Using the configuration file located in ~/.irods/irods_environment.json
        2. If not located, the file given by the environment variable IRODS_ENVIRONMENT_FILE
    To help in this configuration, a method, create_irods_env() can be used.

    Once this has been done one time, there will be no need for using this method on local machines.
    If you are working within Docker containers or VMs environment, you may need to call this at the
    beginning of each task.
    '''

    if not skip_config_irods:
        print('\n------------------------IRODS CONFIGURATION------------------------\n')
        
        # Place your username here:
        username = 'noecarras'
        
        # Calling this function will initiate the environement file with the proper fields
        env_path = create_irods_env(username)
        print(f'configuration written to {env_path}')
        
        # We can check that the environement file is looking good
        env_content = subprocess.run(['cat', env_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print('irods environment file is: \n', env_content)


    # ======================= CACHE CONFIGURATION ======================= 
    '''
    To configure the cache, open the file /utils/global_variables.py.
    Then set the variable local_path to the root of the folder you will be working into.
    The cache creation will generate 2 folders:
        <your-project-root>/temp_cache
        <your-project-root>/long_cache
    
    The long cache will hold the files referencing the csv files giving the address of files to download.
    The temp cache will hold files 1 by 1, and will be cleared between each call to the next() method of the FileIterator class.
    '''

    if not skip_config_cache:
        print('\n------------------------CACHE CONFIGURATION------------------------\n')
        
        # initiate the temporary cache folder like this:
        init_cache()

        # calling the init cache function as such targets the long lasting cache folder
        init_cache(long=True)

        # looking at the structure of your root folder, you should see both folders having been created:
        folder_structure = subprocess.run(['cd', local_folder, '&&', 'ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print('Your folder structure now looks like: \n', folder_structure)

