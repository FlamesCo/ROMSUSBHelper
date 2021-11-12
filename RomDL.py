## this is ROM downloader for the ROMs in the ROMs folder
# It downloads roms from github into a folder called ROMs on your documents folder
# It also downloads the latest version of the ROMs from the github repo
## (C) 2019 by Ralf Westram (amgine.de)
print("Welcome to the ROM Manager 0.1a")
print("This ROM Manager downloads all SNES games from github to your PC or Mac")
print("It also downloads the latest version of the ROMs from the github repo")
print("This is a beta version, so please report any bugs you find")
## get the path to the documents folder
import os
import sys
import shutil
import subprocess
import time
import urllib.request
import zipfile
import tarfile
import glob
import re
import platform
import getpass
import datetime
import json
import requests
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import urllib.error
import urllib.parse
# sync the script with github and ask the user what rom to download
# get the url to the rom 
# download the rom
# unzip the rom
print("Downloading the latest version of the ROMs from github")
print("This may take a while, please be patient")
print("")
urllib = urllib.request.urlopen("https://github.com/FlamesLLC/ROMSUSBHelper")

## this is a wip in progress rom  downloader v0.1a