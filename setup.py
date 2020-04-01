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
if(input("Start wildcard install? (Y/n)").contains('n')):
    print(error + "Aborting.")
    exit()
os.chdir(os.path.dirname(__file__))

print(info + "Making ~/bin directory")
os.mkdir(os.path.expanduser("~/bin"))

print(info + "Copying files into ~/bin directory")
copyfile("wild.py", os.path.expanduser("~/bin/wild.py"))
copyfile("wild", os.path.expanduser("~/bin/wild"))

print(info + "Changing permissions of files in ~/bin")
os.chmod(os.path.expanduser("~/bin/wild.py"), 744)
os.chmod(os.path.expanduser("~/bin/wild"), 744)

print(info + "Adding code completion line to .bashrc")
with open(os.path.expanduser("~/.bashrc"), "a") as file:
    file.write("complete -o nospace -C ~/bin/wild.py wild")

print(info + "Done!")

