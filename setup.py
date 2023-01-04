#!/usr/bin/env python3
"""
extended-logger library
"""

from setuptools import setup, find_packages

setup(
    name="extended-logger",
    author="Marc Averbeck",
    author_email="ghostcode1337@gmx.com",
    description="Extended logging library",
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    license_files=('LICENSE',),
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[],
    setup_requires=["setuptools_scm"],
    use_scm_version=True
)
