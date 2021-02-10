"""test utilities/fixtures"""
import pathlib

import pytest


@pytest.fixture()
def create_files():
    """shared fixture for making files, expects a tmp_file handle"""

    def _create_files(
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

    return _create_files
