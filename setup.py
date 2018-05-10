#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    author="Gui Talarico",
    author_email='gui.talarico+pip@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Curses Windows Binaries",
    license="Public Domain",
    long_description=readme,
    include_package_data=True,
    keywords='curses,windows',
    name='curses-win',
    url='https://github.com/gtalarico/curses-win',
    version='0.2.0',
    zip_safe=False,
)
