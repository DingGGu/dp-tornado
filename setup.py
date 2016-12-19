# -*- coding: utf-8 -*-
"""
MVC Web Application Framework with Tornado, Python 2 and 3

To install the package run:

    pip install dp-tornado


Run
-----

    $ pip install virtualenv
    $ virtualenv ./venv
    $ . ./venv/bin/activate
    $ pip install dp-tornado
    $ dp4p init --path app

"""


import sys
import os


from setuptools import setup

try:
    from setuptools.command.install import install

except ImportError:
    from distutils.command.install import install


with open('dp_tornado/version.py', 'r') as fp_v:
    for c in fp_v.read().split('\n'):
        exec(c)


dp_project_name = 'dp-tornado'
dp_version = __version__
dp_github_url = 'http://github.com/why2pac/dp-tornado'
dp_license = 'MIT'

dp_author = 'Parker'
dp_author_email = 'oss@dp.farm'

dp_maintainer = dp_author
dp_maintainer_email = dp_author_email

dp_description = 'MVC Web Application Framework with Tornado.'


install_requires = [
        'tornado==4.4.2',
        'redis==2.10.5',
        'requests==2.12.4',
        'croniter==0.3.13',
        'pytz==2016.10',
        'pycrypto==2.6.1',
        'boto3==1.4.2',
        'SQLAlchemy==1.1.4',
        'Pillow==3.4.2',
        'wand==0.4.4',
        'validate_email==1.3',
        'BeautifulSoup4==4.5.1',
        'lxml==3.7.0',
        'httpagentparser==1.7.8',
        'validators==0.11.1',
        'CyMySQL==0.8.9',
        # , 'selenium'
    ]


if sys.version_info[0] <= 2:
    install_requires.append('futures==3.0.5')


# Will not install dependencies when it starts from readthedocs.
if os.environ.get('READTHEDOCS') == 'True':
    exec('install_requires = []')


setup(
    name=dp_project_name,
    version=dp_version,
    url=dp_github_url,
    license=dp_license,
    author=dp_author,
    author_email=dp_author_email,
    maintainer=dp_maintainer,
    maintainer_email=dp_maintainer_email,
    description=dp_description,
    long_description=__doc__,
    packages=['dp_tornado'],
    include_package_data=True,
    install_requires=install_requires,
    keywords=['MVC', 'Web Application Framework'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ],
    entry_points={
        'console_scripts': [
            'dp4p = dp_tornado.cli:main'
        ]
    }
)
