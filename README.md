# File Iterator and IRODS Utility classes

This repo gives utility classes for handling file interactions with CIRCLES CyVerse.

It allows:

*(version 1.1.2)*
- Communication with CyVerse's fileshare (ls, cd, pwd)
- I/O Commands through IRODS
- Iterating over files from CyVerse
- Cache handling

*(version 1.0.4, availbale on the branch stable-v1.0.4)*
- perform event analysis on a file
- perform event analysis on all the files of a file exploration


## External links

To see examples of usage of this package, you can go to: https://github.com/codingrosquick/file_iterator_code_examples

To see the published package on PyPI, go to: https://pypi.org/project/circles-file-iterator/



## CONFIGURATION [if pulled repostory from PyPI]

To install everything properly, run the following command:
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install circles-file-iterator
python3 -m pip uninstall twine
python3 -m pip install strym==0.4.17
python3 -m circles_file_iterator
```

You may need to install IRODS command line afterwards if you haven't done it.
You can do so by running the following commands, and inputting the desired fields:
```
wget https://files.renci.org/pub/irods/releases/4.1.10/ubuntu14/irods-icommands-4.1.10-ubuntu14-x86_64.deb
sudo apt-get install -y ./irods-icommands-4.1.10-ubuntu14-x86_64.deb
iinit
```
you can find more information on this topic at this address: https://irods.org/download/.

If you use windows or mac OS, you can download the executable files, install, then execute the command:
```
iinit
```

## Rebuilding the package for PyPI

To rebuild the package for publishing, do the following steps:
1. Go to ```setup.py```, increase the version number.
2. Do the same in ```circles_file_iterator/__init__.py```
3. Run the following command to build the executable:
```
python3 -m build
```
4. Run the following command to push those changes to PyPI
```
twine upload --repository pypi dist/* --verbose
```







## CONFIGURATION [if pulled repostory from GitHub]

*QUICKNOTE:* Some of this configuration may be outdated or not stable depending on your os.

You don't need to bother with those configurations if you pull this as a package from PyPI.


### Install the packages

To install the required packages, simply run in the terminal:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### IRODS environment

To connect to CyVerse, you need your profile to be set.To retrieve this profile, the irods client tries:
    1. Using the configuration file located in ~/.irods/irods_environment.json
    2. If not located, the file given by the environment variable IRODS_ENVIRONMENT_FILE

WARNING: If your access to CyVerse through IRODS already works locally, there would be no need to do this step.

Once this has been done one time, there will be no need for using this method on local machines.

If you are working within Docker containers or VMs environment, you may need to call this at the beginning of each task.


### Cache folders

To configure the cache, open the file ```/global_variables/global_variables.py```.

Then set the variable ```local_path``` to the root of the folder you will be working into.
Check out the file ```example_irods``` for an example of such configuration.







