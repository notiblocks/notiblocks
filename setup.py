from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Logging library for the impatient'
LONG_DESCRIPTION = 'Easy way to make your terminal logs more colorful.'

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