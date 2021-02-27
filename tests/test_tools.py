"""tests for unicorn_sort.tools"""
import pathlib

import pytest

from unicorn_sort import tools


def test_list_files_default(tmp_path, create_files):
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
@pytest.mark.parametrize(
    "filename,expected_rating",
    [
        ("7D2_1974.xmp", 3),
        ("R5A_4552.xmp", 3)
    ]
)
def test_parse_xmp(testdata, filename, expected_rating):
    result = tools.parse_xmp(testdata/filename)

    assert result["xmp:Rating"] == str(expected_rating)
