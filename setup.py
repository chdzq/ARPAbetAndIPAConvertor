#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
from datetime import date

from setuptools import setup, find_packages

# --- import your package ---
import arpabetandipaconvertor as package

if __name__ == "__main__":
    # --- Automatically generate setup parameters ---
    # Your package name
    PKG_NAME = package.__name__

    # Long description will be the body of content on PyPI page
    try:
        LONG_DESCRIPTION = open("README.rst", "rb").read().decode("utf-8")
    except:
        LONG_DESCRIPTION = "No long description!"

    PACKAGES, INCLUDE_PACKAGE_DATA, PACKAGE_DATA, PY_MODULES = (
        None, None, None, None,
    )

    # It's a directory style package
    if os.path.exists(__file__[:-8] + PKG_NAME):
        # Include all sub packages in package directory
        PACKAGES = [PKG_NAME] + ["%s.%s" % (PKG_NAME, i)
                                 for i in find_packages(PKG_NAME)]

        # Include everything in package directory
        INCLUDE_PACKAGE_DATA = True
        PACKAGE_DATA = {
            "": ["*.*"],
        }

    # It's a single script style package
    elif os.path.exists(__file__[:-8] + PKG_NAME + ".py"):
        PY_MODULES = [PKG_NAME, ]

    # Read requirements.txt, ignore comments
    try:
        REQUIRES = list()
        f = open("requirements.txt", "rb")
        for line in f.read().decode("utf-8").split("\n"):
            line = line.strip()
            if "#" in line:
                line = line[:line.find("#")].strip()
            if line:
                REQUIRES.append(line)
    except:
        REQUIRES = list()

    setup(
        name=PKG_NAME,
        description='ARPAbet和ipa之间互相转换的工具',
        long_description=LONG_DESCRIPTION,
        version='1.0.2',
        author='zhanqgi',
        author_email='zhangqi.248@gmail.com',
        packages=PACKAGES,
        include_package_data=INCLUDE_PACKAGE_DATA,
        package_data=PACKAGE_DATA,
        py_modules=PY_MODULES,
        url='https://github.com/chdzq/ARPAbetAndIPAConvertor.git',
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: MIT License',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
        license='MIT License',
        install_requires=REQUIRES,
        keywords='IPA ARPAbet ipa arpabet convert ARPAbetAndIPAConvertor',
    )

"""
Appendix
--------
::
Frequent used classifiers List = [
    "Development Status :: 1 - Planning",
    "Development Status :: 2 - Pre-Alpha",
    "Development Status :: 3 - Alpha",
    "Development Status :: 4 - Beta",
    "Development Status :: 5 - Production/Stable",
    "Development Status :: 6 - Mature",
    "Development Status :: 7 - Inactive",
    "Intended Audience :: Customer Service",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Financial and Insurance Industry",
    "Intended Audience :: Healthcare Industry",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Legal Industry",
    "Intended Audience :: Manufacturing",
    "Intended Audience :: Other Audience",
    "Intended Audience :: Religion",
    "Intended Audience :: Science/Research",
    "Intended Audience :: System Administrators",
    "Intended Audience :: Telecommunications Industry",
    "License :: OSI Approved :: BSD License",
    "License :: OSI Approved :: MIT License",
    "License :: OSI Approved :: Apache Software License",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "Natural Language :: English",
    "Natural Language :: Chinese (Simplified)",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 2 :: Only",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3 :: Only",
]
"""
