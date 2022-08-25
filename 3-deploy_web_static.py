#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the
contents of the web_static folder of the AirBnB Clone repo,
using the function do_pack and that distributes an archive to
your web servers, using the function do_deploy
"""

from datetime import datetime
from fabric.api import local, put, run, env
from os.path import exists

env.hosts = ['18.207.125.211', '3.91.17.213']


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


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    try:
        fileFullName = archive_path.split("/")[-1]
        fileName = fileFullName.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, fileName))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fileFullName, path, fileName))
        run('rm /tmp/{}'.format(fileFullName))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, fileName))
        run('rm -rf {}{}/web_static'.format(path, fileName))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, fileName))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
