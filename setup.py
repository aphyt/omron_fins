import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fins",
    version="1.0.4",
    author="Joseph Ryan",
    author_email="jr@aphyt.com",
    description="A library to communicate with Omron controllers using Factory Intelligent Network Service (FINS)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aphyt/omron_fins",
    packages=setuptools.find_packages(exclude=("tests", "docs", "examples")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
