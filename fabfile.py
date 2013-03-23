from packager import Deployment
from fabric.api import env


env.hosts = ['localhost:41022']


def deb():
    deploy = Deployment("wb", "flask-native-package", 'git@github.com:whelmingbytes/flask-native-package.git', build_user='vagrant')
    for attr in dir(deploy):
        if not attr.startswith('_'):
            print attr, ':', getattr(deploy, attr)
    print
    deploy.prepare_python_app(requirements_file='requirements/base.txt')
    deploy.build_deb()
