from fabric.api import task, env
from parcel.deploy import Deployment
from parcel import distro
from parcel import tools


env.app_name = 'flask-native-package'
env.user = 'root'


@task
def deb():
    deploy = Deployment(
        env.app_name,
        build_deps=['python-virtualenv', 'python-pip'],
        base='/opt/webapps/wb/flask-native-package',
        arch=distro.Ubuntu(),
        version="0.0.1"
    )

    deploy.add_preinst(['service %s stop' % env.app_name])
    deploy.add_postinst(['service %s start' % env.app_name])
    deploy.prepare_app()

    #this should be built into parcel, or needs an Upstart(Depployment)
    tools.rsync([deploy.path+'/debian/'],deploy.root_path,rsync_ignore='.rsync-ignore')
    deploy.build_package()
