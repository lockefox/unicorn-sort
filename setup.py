"""package setup for unicorn-sort"""
from codecs import open
from pathlib import Path
from setuptools import setup, find_packages

__package_name__ = "unicorn-sort"
__library_name__ = "unicorn_sort"
HERE = Path(__file__).resolve().parent

with open("README.md", "r", "utf-8") as f:
    __readme__ = f.read()

with open(HERE / __library_name__ / "VERSION", "r", "utf-8") as f:
    __version__ = f.read().strip()

setup(
    name=__package_name__,
    description="Helper for sorting and backing up photo file dumps",
    version=__version__,
    long_description=__readme__,
    long_description_content_type="text/markdown",
    author="John Purcell",
    author_email="jpurcell.ee@gmail.com",
    packages=find_packages(),
    package_data={"": ["README"], __library_name__: ["VERSION"],},
    entry_points={"console_scripts": [f"unicorn={__library_name__}.cli:run",]},
    install_requires=["plumbum",], # "exifread", "canon-cr3"],
    extras_require={"dev": {"tox", "tox-travis", "black",}},
)
