#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the
contents of the web_static folder of the AirBnB Clone repo,
using the function do_pack and that distributes an archive to
your web servers, using the function do_deploy
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['18.207.125.211', '3.91.17.213']


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
