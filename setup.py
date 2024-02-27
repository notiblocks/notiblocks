from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Logging library for the impatient'
LONG_DESCRIPTION = 'A package that allows to log colorful messages on the terminal.'

# Setting up
setup(
    name="notiblocks",
    version=VERSION,
    author="D4rkC47 (Deyan Sirakov)",
    author_email="dvs_sec@proton.me",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'logging', 'warning', 'terminal', 'ansi', 'color'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)