# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from setuptools import setup
from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

# Get version info
ABOUT = {}
with open(path.join(HERE, "datadog_checks", "nifi", "__about__.py")) as f:
    exec(f.read(), ABOUT)

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# Parse requirements
def get_requirements(fpath):
    with open(path.join(HERE, fpath), encoding='utf-8') as f:
        return f.readlines()

CHECKS_BASE_REQ = 'datadog_checks_base'

setup(
    name='datadog-nifi',
    version=ABOUT["__version__"],
    description='This check collects runtime metrics from Nifi',
    long_description=long_description,
    keywords='datadog agent Nifi check',
    url='https://github.com/DataDog/integrations-core',
    author='Sean m',
    author_email='sean@beamery.com',
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    packages=['datadog_checks.nifi'],

    # Run-time dependencies
    install_requires=[CHECKS_BASE_REQ],
    setup_requires=['pytest-runner', ],
    tests_require=get_requirements('requirements-dev.txt'),

    # Extra files to ship with the wheel package
    package_data={'datadog_checks.collect runtime metrics from nifi': ['conf.yaml.example']},
    include_package_data=True,
)