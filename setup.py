#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Documentation
-------------

The full documentation is at https://ebay.readthedocs.org.
"""

import os
import sys
import re


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools.command.test import test as TestCommand

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)


_version_re = re.compile(r"(?<=^__version__ = \')[\w\.]+(?=\'$)", re.U | re.M)
with open('ebay/__init__.py', 'rb') as f:
    version = _version_re.search(f.read().decode('utf-8')).group()

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

# TODO: put package requirements here
requirements = []

# TODO: put package test requirements here
test_requirements = ['pytest', 'mock']

# @:off
setup(
    name='ebay',
    version=version,
    description="A python package for simple access to eBay's API.",
    long_description=readme + '\n\n' + __doc__ + '\n\n' + history,
    author="Manu Phatak",
    author_email='bionikspoon@gmail.com',
    url='https://github.com/bionikspoon'
        '/ebay',
    packages=[
        'ebay',
    ],
    package_dir={'ebay':
                 'ebay'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    cmdclass={'test': PyTest},
    keywords='ebay',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
# @:on