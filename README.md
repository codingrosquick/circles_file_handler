# File Iterator and IRODS Utility classes

### Timeline
This repo gives utility classes for handling file interactions with CIRCLES CyVerse.

The package will be published on Pip once stable and tested.


## CONFIGURATION

### IRODS environment

To connect to CyVerse, you need your profile to be set.To retrieve this profile, the irods client tries:
    1. Using the configuration file located in ~/.irods/irods_environment.json
    2. If not located, the file given by the environment variable IRODS_ENVIRONMENT_FILE

To help in this configuration, a method, create_irods_env() can be used.
Check out the file ```code_examples/example_irods``` for an example of such configuration.

Once this has been done one time, there will be no need for using this method on local machines.

If you are working within Docker containers or VMs environment, you may need to call this at the beginning of each task.


### Cache folders

To configure the cache, open the file ```/utils/global_variables.py```.

Then set the variable local_path to the root of the folder you will be working into.
Check out the file ```code_examples/example_irods``` for an example of such configuration.










