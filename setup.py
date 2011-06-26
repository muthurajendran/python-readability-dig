#!/usr/bin/env python
from distutils.core import setup


setup(
    name="lxml-readability",
    author="Yuri Baburov",
    author_email="burchik+github@gmail.com",
    description="python port of arc90's readability bookmarklet",
    long_description=open("README").read(),
    license="Apache License 2.0",
    url="http://github.com/buriy/python-readability",
    packages=[
        "lxml_readability",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
