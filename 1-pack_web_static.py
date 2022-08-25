#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the
contents of the web_static folder of the AirBnB Clone repo,
using the function do_pack
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a .tgz file"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        fileName = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fileName))
        return fileName
    except Exception:
        return None
