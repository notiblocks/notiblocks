from setuptools import setup, find_packages
import subprocess
import os

VERSION="0.0.3"
DESCRIPTION = 'Logging library for the impatient'
long_description=""

with open('README.md', 'r', encoding='utf-8') as fd:
    long_description=fd.read()

# Setting up
setup(
    name="notiblocks",
    version=VERSION,
    author="D4rkC47 (Deyan Sirakov)",
    author_email="dvs_sec@proton.me",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'logging', 'warning', 'terminal', 'ansi', 'color'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
