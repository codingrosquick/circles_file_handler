# File Iterator and IRODS Utility classes

### Timeline
This repo gives utility classes for handling file interactions with CIRCLES CyVerse.

It allows:
- Communication with CyVerse's fileshare (ls, cd, pwd)
- I/O Commands through IRODS
- Iterating over files from CyVerse
- Cache handling


## CONFIGURATION [if pulled repostory from PyPI]

To install everything properly, run the following command:



## CONFIGURATION [if pulled repostory from GitHub]

### Install the packages

To install the required packages, simply run in the terminal:
```
python3 -m venv venv
source venv/bin/activate
pip install requirements.txt
```


### IRODS environment

To connect to CyVerse, you need your profile to be set.To retrieve this profile, the irods client tries:
    1. Using the configuration file located in ~/.irods/irods_environment.json
    2. If not located, the file given by the environment variable IRODS_ENVIRONMENT_FILE

To help in this configuration, a method, create_irods_env() can be used.
Check out the file ```code_examples/example_irods``` for an example of such configuration.

WARNING: If your access to CyVerse through IRODS already works locally, there would be no need to do this step.

Once this has been done one time, there will be no need for using this method on local machines.

If you are working within Docker containers or VMs environment, you may need to call this at the beginning of each task.


### Cache folders

To configure the cache, open the file ```/global_variables/global_variables.py```.

Then set the variable ```local_path``` to the root of the folder you will be working into.
Check out the file ```code_examples/example_irods``` for an example of such configuration.










