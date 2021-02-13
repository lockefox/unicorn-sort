"""test_cli: test cli's work as advertised"""
import os
import pytest

from plumbum import local

from unicorn_sort import __version__, cli


class TestStashVid:
    stashvid = local[f'{os.environ["TOX_ENV_DIR"]}/bin/{cli.__stash_vid__}']

    def test_stashvid_version(self):
        """asserts -v works"""
        output = self.stashvid("-v")

        print(output)
        assert output.strip() == f"{cli.__stash_vid__} {__version__}"

    def test_stashvid_help(self):
        """asserts help doesn't blow up"""
        output = self.stashvid("-h")

        assert output.strip()

    def test_stashvid_happypath(self, tmp_path, create_files):
        """actually runs the real CLI for testing"""
        move_files = ["dummy.mp4", "fake.mp4"]

        stay_files = [
            "ignore_me.CR2",
            "ignore_me_too.cr3",
            "ignore_me_also.xmp",
        ]

        ignore_dirs = ["ignore_dir"]

        create_files(tmp_path, move_files + stay_files, ignore_dirs)

        print(tmp_path.absolute())
        self.stashvid(
            f"--source-dir={str(tmp_path.absolute())}",
            f"--dest-dir={str(tmp_path.absolute() / 'VIDS')}",
        )

        print(list(file for file in (tmp_path / "VIDS").iterdir()))
        file_list = set([file.name for file in (tmp_path / "VIDS").iterdir() if file.is_file()])

        assert set(move_files) == file_list
