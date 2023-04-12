from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name = "fasthr",
    version = "1.1",
    author = "Fan Zou",
    author_email = "fuz64@psu.edu",
    description = "A Python function that efficiently and accurately calculates hardness ratios for X-ray sources using a Bayesian approach",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/fanzou99/FastHR",
    install_requires = ["numpy", "scipy"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
