#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import shells

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = shells.__version__

if sys.argv[-1] == 'publish':
    try:
        import wheel    # noqa
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-shells',
    version=version,
    description='Better shells for your manage.py',
    long_description=readme + '\n\n' + history,
    author='Tzu-ping Chung',
    author_email='uranusjr@gmail.com',
    url='https://github.com/uranusjr/django-shells',
    packages=[
        'shells',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license='BSD',
    zip_safe=False,
    keywords='django-shells',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
