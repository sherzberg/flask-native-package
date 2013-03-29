from fabric.api import *
from parcel.deploy import Deployment
from parcel import distro

env.app_name = 'flask-native-package'
env.user = 'root'


@task
def deb():
    deploy = Deployment(env.app_name, build_deps=['python-virtualenv', 'python-pip'], base='/opt/webapps/wb/testapp', arch=distro.Ubuntu())
    deploy.prepare_app()
    deploy.build_package()
