#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '0.1.0'

setup(
    name='github_notifier',
    python_requires=">=3",
    version=__version__,
    packages=find_packages(),
    author="Jay MOULIN",
    author_email="jaymoulin@gmail.com",
    description="Github Notifier",
    long_description=open('README.rst').read(),
    install_requires=[""],
    include_package_data=True,
    url='http://github.com/femtopixel/github-notifier/',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: File Sharing",
        "Topic :: Home Automation",
        "Topic :: Internet",
    ],
    entry_points={
        'console_scripts': [
            'github-notifier = github_notifier.cli:main',
        ],
    },
    license="MIT",
)
