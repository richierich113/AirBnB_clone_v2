script to automate deployment """

from fabric.api import *
import os
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'


def do_pack():
    """ Pack up our web_static """
    try:
        os.makedirs('versions', exist_ok=True)
        time_format = "%Y%m%d%H%M%S"
        now = datetime.now().strftime(time_format)
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(now))
        return "versions/web_static_{}.tgz".format(now)
    except Exception as e:
        return None


def do_deploy(archive_path):
    """ Deploy our packed archive """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_folder = '/data/web_static/releases/{}'.format(
            archive_name.split('.')[0])

        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}'.format(archive_folder))
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_name, archive_folder))
        run('sudo rm /tmp/{}'.format(archive_name))
        run('sudo mv {}/web_static/* {}/'.format(archive_folder, archive_folder))
        run('sudo rm -rf {}/web_static'.format(archive_folder))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(archive_folder))
        print('New version deployed!')
        return True
    except Exception as e:
        return False


def do_clean(number=0):
    """ Clean up old deployments """
    if int(number) < 2:
        number = 1
    else:
        number = int(number)

    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs rm -rf'.format(number + 1))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number + 1))
