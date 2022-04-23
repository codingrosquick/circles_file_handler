# CYVERSE PATH
import os

cyverse_path_server_resources = '/iplant/home/noecarras/resources_file_iterator/'
cyverse_path_server_resources_default = '/iplant/home/noecarras/resources_file_iterator/default/'
cyverse_path_server_resources_user = '/iplant/home/noecarras/resources_file_iterator/user/'
cyverse_path_server_resources_test = '/iplant/home/noecarras/resources_file_iterator/test/'

# LOCAL CACHES
# NOTE: use absolute path to avoid issues
# TODO: remove my personal path when publishing
# local_folder = '<path-to-your-project>'
# local_user_folder = '<path-to-your-user-folder>'
local_folder = '/Users/noecarras/Documents/03_Berkeley_EECS/cours/Capstone_RL_validation/filehandler/circles_file_handler'

local_temp_folder = os.path.join(local_folder, 'temp_cache')
local_long_folder = os.path.join(local_folder, 'long_cache')

