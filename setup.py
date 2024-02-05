# coding: utf-8
import io
import os
import re

from setuptools import find_packages, setup


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

about = {}
with open(os.path.join(CURRENT_DIR, 'scrapydweb', '__version__.py')) as f:
    exec(f.read(), about)

with io.open("README.md", 'r', encoding='utf-8') as f:
    long_description = re.sub(r':\w+:\s', '', f.read())  # Remove emoji


setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    description=about['__description__'],

    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=find_packages(exclude=("tests", )),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=2.7, ==3.11",
    install_requires=[
        "APScheduler",  # Aug 15, 2018
        "click",  # Sep 26, 2018
        "colorama",  # Oct 10, 2018
        "Flask",  # May 2, 2018
        "Flask-Compress",  # Jan 5, 2017
        "Flask-SQLAlchemy",  # Apr 25, 2019
        "idna",  # Jun 11, 2018    
        "itsdangerous",  # Oct 27, 2018
        "Jinja2",  # Nov 9, 2017
        "logparser",
        "MarkupSafe",  # Feb 24, 2019
        "pexpect",  # Apr 7, 2019
        "ptyprocess",  # Jun 22, 2018
        "pytz",  # Jan 7, 2019
        "requests",  # Dec 10, 2018
        "setuptools",  # Dec 11, 2018
        "six",  # Dec 10, 2018
        "SQLAlchemy",  # Mar 31, 2021
        "tzlocal",  # Dec 1, 2017
        "w3lib",  # Jan 25, 2018
        "Werkzeug",  # Jan 1, 2018
    ],

    entry_points={
        "console_scripts": {
            "scrapydweb = scrapydweb.run:main"
        }
    },

    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
