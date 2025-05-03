from setuptools import setup, find_packages

with open("README") as f:
    long_description = f.read()

setup(
    name="ContentOrganizer",
    version="0.1",
    packages=find_packages(),
    description="ContentOrganizer is a local-first, AI-powered tool that intelligently analyzes and organizes your image files into meaningful folders based on visual content—securely, privately, and with zero cloud dependencies.",
    url="https://github.com/jharri34/ContentOrganizer",
    author="jharri34",
    long_description=long_description,
)