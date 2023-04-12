from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name = "fasthr",
    version = "1.0.0",
    author = "Fan Zou",
    author_email = "fuz64@psu.edu",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/fanzou99/FastHR",
    packages = find_packages(),
    install_requires = ["numpy", "scipy"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
