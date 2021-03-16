import os
import re

PACKAGE = "finalsa"

from setuptools import setup

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(os.path.join(package, "__init__.py")) as f:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", f.read()).group(1)


def get_long_description():
    """
    Return the README.
    """
    with open("README.md", encoding="utf8") as f:
        return f.read()

def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


setup(
    name='finalsa-services-connector',
    version='1.0.0',
    url='https://github.com/finalsa/finalsa-flask-models/',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license='BSD',
    author='Luis Diego Jiménez Delgado',
    author_email='luis@finalsa.com',
    description='Handler for finalsa services',
    packages=get_packages(PACKAGE),
    package_data={PACKAGE: ["py.typed"]},
    zip_safe=False,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'requests',
    ],
    classifiers=[
    ]
)