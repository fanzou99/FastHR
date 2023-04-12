from setuptools import setup

setup(
	name = "fasthr",
    version = "1.0",
    author = "Fan Zou",
    author_email = "fuz64@psu.edu",
    description = "A Python function that efficiently and accurately calculates hardness ratios for X-ray sources using a Bayesian approach",
    url = "https://github.com/fanzou99/FastHR",
    install_requires = ["numpy", "scipy"],
    classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
	]
)