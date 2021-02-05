"""tests for unicorn_sort.tools"""
import pathlib

import pytest

from unicorn_sort import tools


def create_files(
    host_dir: pathlib.Path, test_files: list = None, test_dirs: list = None
) -> pathlib.Path:
    """helps build files for test case.

    Args:
        host_dir (:obj:`pathlib.Path`): pytest tmpdir handler
        test_files (list): list of filenames to create
        test_dirs (list: optional): list of dirnames to create

    Returns:
        pathlib.Path: path to host_dir

    """
    if not test_dirs:
        test_dirs = []
    for file in test_files:
        with open(host_dir / file, "w") as f:
            f.write("test_file")

    for dirname in test_dirs:
        (host_dir / dirname).mkdir()

    return host_dir


def test_list_files_default(tmp_path):
    """list_files"""
    test_files = [
        "test_file1.cr2",
        "test_file2.cr3",
        "test_file3.CR2",
    ]
    extra_files = [
        "ignore_file1.txt",
    ]
    test_dirs = ["ignore_dir"]

    create_files(tmp_path, test_files + extra_files, test_dirs)

    files = tools.list_files(tmp_path)

    file_list = set(file.path.name for file in files)
    assert file_list == set(test_files)
