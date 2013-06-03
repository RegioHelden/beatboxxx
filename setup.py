# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages

setup(
    name='beatboxxx',
    packages=find_packages(),
    version='21.0',  # be sure to update the version in _beatbox.py too
    description="A Python client for the Saleforce.com SOAP API",
    author="RegioHelden GmbH, Simon Fell et al",
    author_email='opensource@regiohelden.de',
    url="https://github.com/RegioHelden/beatbox",
    keywords="python salesforce salesforce.com",
    license="GNU GENERAL PUBLIC LICENSE Version 2",
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable"
    ],
    include_package_data=True,
    long_description=(
        open('README.txt').read() +
        "\n" +
        open('CHANGES.txt').read(),
    ),
    zip_safe=False,
)
