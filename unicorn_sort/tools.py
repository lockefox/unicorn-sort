"""utilities for processing files"""
from collections import namedtuple
import pathlib
import typing

from libxmp import XMPMeta, consts
from plumbum import local

# Note, requires exiftool cli: https://exiftool.org/
exiftool = local["exiftool"]

image_file = namedtuple(
    "ImageFile",
    ["path", "name", "ext"],
)

SUPPORTED_FILES = [
    ".cr2",
    ".cr3",
    "xmp",
]


def list_files(file_pathlib: pathlib.Path, file_filter: list = None) -> typing.List[image_file]:
    """lists all files in a directory given a specific filter"""
    if not file_filter:
        file_filter = SUPPORTED_FILES
    return [
        image_file(file, file.stem, file.suffix.lower())
        for file in file_pathlib.iterdir()
        if file.is_file() and file.suffix.lower() in file_filter
    ]
