# Python Berichtsheft Generator - generator for a portfolio needed in most german apprenticeships
# Copyright (C) 2021  Timon Schneider
# mail@timon-schneider.net
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import py2exe, sys

sys.argv.append('py2exe')

def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    file = open(filepath, 'r')
    return file.read()

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = ["cli.py"],
    zipfile = None,
    name="Python Berichtsheft Generator",
    version="1.0.1",
    description="generator for a portfolio needed in most german apprenticeships",
    long_description=read('README'),
    long_description_content_type="text/markdown",
    url="https://timon-schneider.net/PBG",
    author="Timon Schneider",
    author_email="mail@timon-schneider.net",
    license="GNU General Public License v3.0",
    classifiers=[
        "Environment :: Console"
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
    #packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyMuPDF"
    ],
)
