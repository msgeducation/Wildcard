#!/usr/bin/python3
import shutil
import os

class COLORS:
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"
    YELLOW = "\033[93m"
info = COLORS.YELLOW + "[+] " + COLORS.RESET
error = COLORS.RED + "[-] " + COLORS.RESET
art = \
"""
 *     *       #         #  ##  ##      #####    ######      ##      #####   #####         *     *
  *   *        ##       ##  ##  ##      ##  ##   ##         ####     ##  ##  ##  ##         *   *
   * *          #       #   ##  ##      ##   #   ##         #  #     ##  #   ##   #          * *
*********       ##  #  ##   ##  ##      ##   ##  ##        ##  ##    ## ##   ##   ##      *********
   * *           #######    ##  ##      ##   ##  ##        ######    ####    ##   ##         * *   
  *   *           ## ##     ##  ######  ##  ##   ##       ##    ##   ## ##   ##  ##         *   *
 *     *          ## ##     ##  ######  #####    ######  ##      ##  ##  ##  #####         *     *
"""
print(COLORS.GREEN + art + COLORS.RESET)
if('n' in input("Start wildcard install? (Y/n)")):
    print(error + "Aborting.")
    exit()
try:
    os.chdir(os.path.dirname(__file__))
except (FileNotFoundError):
    pass


print(info + "Making ~/bin and ~/Wildcard/scripts directory")
try:
    os.mkdir(os.path.expanduser("~/bin"))
except(FileExistsError):
    pass
try:
    os.mkdir(os.path.expanduser("~/Wildcard/scripts"))
except(FileExistsError):
    pass

print(info + "Copying files into ~/bin directory")
os.symlink(os.path.expanduser("~/Wildcard/wild.comp"), os.path.expanduser("~/bin/wild.comp"))
os.symlink(os.path.expanduser('~/Wildcard/wild'), os.path.expanduser("~/bin/wild"))

print(info + "Changing permissions of files in ~/bin")
os.chmod(os.path.expanduser("~/bin/wild.comp"), 0o744)
os.chmod(os.path.expanduser("~/bin/wild"), 0o744)

try:
    open('.status', 'r')
except FileNotFoundError:
    print(info + "Adding code completion line and PATH addition to .bashrc")
    with open(os.path.expanduser("~/.bashrc"), "a") as file:
        file.write("complete -o nospace -C ~/bin/wild.comp wild\nPATH=~/bin:$PATH\n")
    with open('.status', 'w') as file:
        file.write('\n')

print(info + "Done! Please source your .bashrc before testing.")

