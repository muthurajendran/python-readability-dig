#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

lxml_requirement = "lxml"
if sys.platform == 'darwin':
    import platform
    mac_ver = platform.mac_ver()[0]
    mac_ver_no = int(mac_ver.split('.')[1])
    if mac_ver_no < 9:
        print "Using lxml<2.4"
        lxml_requirement = "lxml<2.4"

setup(
    name="readability-dig",
    version="0.5",
    author="Muthu Rajendran R G",
    author_email="muthurajendranrg@gmail.com",
    description="Modified arc90's scraping hub port readability tool for dig data",
    test_suite = "tests.test_article_only",
    long_description=open("README").read(),
    license="Apache License 2.0",
    url="https://github.com/muthurajendran/python-readability-dig",
    download_url = 'https://github.com/muthurajendran/python-readability-dig/tarball/0.1',
    packages=['readability'],
    install_requires=[
        "chardet",
        lxml_requirement,
        "cssselect"
        ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
)
