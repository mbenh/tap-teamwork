#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="tap-teamwork",
    version="0.2.2",
    description="Singer.io tap for extracting data",
    author="Stephen Bailey",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    packages=setuptools.find_packages(),
    py_modules=["tap_teamwork"],
    package_data={"schemas": ["tap_teamwork/schemas/*.json"]},
    entry_points="""
        [console_scripts]
        tap-teamwork=tap_teamwork:main
    """,
    install_requires=[
        "singer-python",
        "requests"
    ],
    include_package_data=True,
)
