flask-native-package
====================

This is a dummy package for testing out some native debian packages. It
uses Parcel to build up a debian package used in native deployments.

This test application requires Upstart only. It packages all the python dependencies
up to run a simple "Hello World" Flask application on port 5000. When you install the
built deb, an upstart script will be installed to run the app on startup.

Setup
=====

First, you must have a machine setup with fmp, python-pip, and
python-virtualenv. This machine must allow root ssh as well. Using a
virtual machine with Vagrant is a good option. This machine is necessary because
it will do all compiling and packaging of dependencies into a deb for us. Parcel
assumes Ubuntu 12.04, so use that...

Build Deb
=========

::

    $ fab -H build-host deb

This will copy code to the build server, create a python virtual environment
with the dependencies defined in requirements.txt, and package everything up
into a native deb.

Install Built Deb
=================

Now you can either install the deb manually:

::

    $ sudo dpkg -i flask-native-package-0.0.1.deb

or a better option would be to host your own apt repository and use apt-get to
install.
