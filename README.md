# Wildcard
A wildcard script for doing common tasks

## Installation
```bash
cd ~
git clone https://github.com/msgeducation/Wildcard.git
cd Wildcard
./setup.py
source ~/.bashrc
```
## Testing
```bash
wild test.sh
```
## Using
To use just type `wild` and the location of the script relative to the scripts directory.  So if you have a moodle maintanence mode script you can run it by typing from anywhere `wild moodle/maintanence.sh --help`.  

## Contributing
To add scripts think about the purpose of the script and how it should be organized.  For example to put moodle in maintanence mode you might make a script called `maintanence.sh` under `~/Wildcard/scripts/moodle/maintanence.sh`.  The script **must** by shell-executable.  
All scripts are called like the this: 
`wild moodle/maintanence.sh --help` will become `/home/$USER/Wildcard/scripts/moodle/maintanence.sh --help`  The script will be passed config file settings via environment variables.  
To make tab-autocompletion you can make a script called `.[name of script to complete].comp`.  For our example that would be `scripts/moodle/.maintanence.sh.comp`.  This script will be called when tab is pressed on the arguments for the script.  It can be written in any language but **must** be shell-executable.  It will be called like this: 
`/home/$USER/Wildcard/scripts/path/to/.file.comp <path-to-file-that-will-run> <name-of-file-that-will-run> <word-under-cursor-to-autocomplete> <previous-word>`
It should return all possible autocompletions filtered by the current text separated by newlines. 
Once you have finished and tested, push or create a pull request for this respository. **Please make sure you do not commit your `wildcard.conf`**
