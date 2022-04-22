import os
import subprocess
from typing import List

# TODO: rehandle cache creation in the beginning
local_temp_folder = '/Users/noecarras/Documents/03_Berkeley_EECS/cours/Capstone_RL_validation/capstone_circles_rl_validation/server/temp_cache/'


def init_cache(cache_kind: str = None):
    '''
    clears the cache if exists and initialise it
    :param kind: subfolder within the temp cache
    :param full_root: root of the cache file if not in ./server/temp_cache Use global variables here!
    :return: cache address
    
    note:   here, the local folder is /server/temp_cache/               (here only the temp folders are used)
            the kind folder is fileshare_exploration for instance       (if you are working with this)
    '''
    try:
        if cache_kind is not None:
            cache_path = os.path.join(local_temp_folder, cache_kind)
        else:
            cache_path = local_temp_folder

        print(cache_path)

        subprocess.run(['rm', '-r', cache_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True)

        subprocess.run(['mkdir', cache_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True)
        
        return cache_path
    
    except Exception as e:
        raise Exception(f'Error while trying to init {cache_kind} in cache.\nFailed on: {e}')


def remove_file_from_cache(file_address: str):
    '''
    Removes one file locally from path
    :param file_address: Path to the file to delete. It needs to be located either in temp_cache or long_cache to be deleted.
    :return: file_address once the file has been deleted.
    '''
    try:
        if (file_address) and ('temp_cache' in file_address):
            subprocess.run(['rm', file_address],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
            return file_address
        
        else:
            raise Exception(f'file not located in cache folders. File has not been deleted')
    
    except Exception as e:
        raise Exception(f'Error while trying to remove {file_address} from Cache.\nFailed on: {e}')

def get_all_files_from_cache_dir(cache_kind: str = None, full_root: str = None) -> List[str]:
    '''
    :param kind: subfolder within the temp cache
    :param full_root: root of the cache file. Use global variables here!
    :return: List of path to the files within the root
    '''
    cache_path = get_cache_path(cache_kind, full_root)
    
    try:
        files = [os.path.join(cache_path, f) for f in os.listdir(cache_path) if os.path.isfile(os.path.join(cache_path, f))]
        return files
    except Exception as e:
        raise Exception(f'Finding files in {cache_path} failed on {e}')


def get_cache_path(cache_kind: str = None, full_root: str = None) -> str:
    '''
    :param kind: subfolder within the temp cache
    :param full_root: root of the folder. Use global variables here!
    :return: actual path of the desired cache
    '''
    if full_root:
        cache_path = full_root
    else:
        cache_path = local_temp_folder

    if cache_kind:
        cache_path = os.path.join(cache_path, cache_kind)  
    return cache_path
