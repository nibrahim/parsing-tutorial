# https://github.com/pypa/sampleproject/blob/master/setup.py

from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()
# .
# ├── README.rst
# ├── setup.py
# └── ssh_client
#     ├── __init__.py
#     └── ssh_client.py


setup(name = "ssh_client",
      version = "0.0.1",
      description = "simple ssh clients",
      long_description = long_description,
      author = "Noufal Ibrahim",
      author_email = "noufal@nibrahim.net.in",
      license = "GPLv3",
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers = ["Development :: 3 - Alpha",
                     "License :: OSI Approves :: GPLv3",
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
                     ],
      keywords = 'ssh paramiko',
      # packages = packages
      packages = ['ssh_client'],
      install_requires = ['paramiko'])
