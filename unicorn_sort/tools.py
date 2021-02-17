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
    ".xmp",
    ".jpg",
    ".jpeg",
    ".dng",
]


def list_files(file_pathlib: pathlib.Path, file_filter: list = None) -> typing.List[image_file]:
    """lists all files in a directory given a specific filter"""
    if file_filter is None:
        file_filter = SUPPORTED_FILES

    if not isinstance(file_filter, list):
        raise TypeError(f"file_filter needs to be list(), was {type(file_filter)}")

    return [
        image_file(file, file.stem, file.suffix.lower())
        for file in file_pathlib.iterdir()
        if file.is_file() and file.suffix.lower() in file_filter
    ]


def find_rating(file_pathlib: pathlib.Path, xmp_section: str = consts.XMP_NS_XMP) -> int:
    """finds the `Rating` value for an image file"""


# (
#     'http://ns.adobe.com/xap/1.0/',
#     '',
#     '',
#     {
#         'VALUE_IS_URI': False,
#         'IS_QUALIFIER': False,
#         'HAS_QUALIFIERS': False,
#         'HAS_LANG': False,
#         'HAS_TYPE': False,
#         'VALUE_IS_STRUCT': False,
#         'VALUE_IS_ARRAY': False,
#         'ARRAY_IS_ORDERED': False,
#         'ARRAY_IS_ALT': False,
#         'ARRAY_IS_ALTTEXT': False,
#         'IS_ALIAS': False,
#         'HAS_ALIASES': False,
#         'IS_INTERNAL': False,
#         'IS_STABLE': False,
#         'IS_DERIVED': False,
#         'IS_SCHEMA': True
#     }
# )
xmp_keydata = namedtuple("XMPKeyData", ["xmp_const", "key", "value", "metadata"])


def parse_xmp(file_pathlib: pathlib.Path, xmp_section: str = consts.XMP_NS_XMP) -> dict:
    """returns xmp results

    Args:
        file_pathlib (:obj:`pathlib.Path`): path to file
        xmp_consts (str: optional): xmp section to parse

    Returns:
        dict: key/value pairs frpm xmp

    """
    xmp = XMPMeta()
    with open(file_pathlib, "r") as f:
        xmp.parse_from_str(f.read())

    attributes = [xmp_keydata(*x) for x in xmp if x[0] == xmp_section]

    return {x.key: x.value for x in attributes}


def parse_exif(file_pathlib: pathlib.Path) -> dict:
    """returns EXIF results"""
