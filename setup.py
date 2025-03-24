from setuptools import setup, find_packages

with open("README") as f:
    long_description = f.read()

setup(
    name="ContentOrganizer",
    version="0.1",
    packages=find_packages(),
    description="SortPhoto is a lightweight, dependency-free image sorting tool that organizes your photos by date or file type",
    url="https://github.com/jharri34/SortPhotos",
    author="jharri34",
    long_description=long_description,
)