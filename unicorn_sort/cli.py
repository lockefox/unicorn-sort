"""main CLI"""

import pathlib
import logging
import sys

from plumbum import cli

from . import __version__, tools

__cli_name__ = "unicorn"
__stash_vid__ = "stashvid"
__stash_jpeg__ = "stashjpeg"


class BaseCLI(cli.Application):
    """parent class for CLIs"""

    @cli.autoswitch(
        str,
        help="Folder full of images CR2/CR3/JPEG",
        envname="UNICORN_SOURCE_DIR",
    )
    def source_dir(self, source_path=pathlib.Path()):
        self._source_dir = pathlib.Path(source_path)

    log_level = cli.SwitchAttr(
        "--log-level",
        cli.Set("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"),
        default="INFO",
        help="verbosity level",
    )

    verbose = cli.Flag(
        ["-V", "--verbose"],
        help="toggle verbose logging",
    )
    _logger = None

    @property
    def logger(self):
        if self._logger is not None:
            return self._logger

        logger = logging.getLogger(self.PROGNAME)
        if self.verbose:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "%(asctime)s [%(levelname)s - %(filename)s:%(funcName)s:%(lineno)s] %(message)s"
            )
            handler.setFormatter = formatter
            logger.addHandler(handler)
        logger.setLevel(logging.getLevelName(self.log_level.upper()))
        self._logger = logger
        return self._logger


class StashVideo(BaseCLI):
    """mini cli: copy mp4s into their own folder"""

    PROGNAME = __stash_vid__
    VERSION = __version__

    _dest_dir = pathlib.Path() / "VIDS"

    @cli.autoswitch(str, help="where to copy all mp4s")
    def dest_dir(self, dest_path=_dest_dir):
        self._dest_dir = pathlib.Path(dest_path)

    def main(self):
        self.logger.info("Hello World")

        files = tools.list_files(self._source_dir, file_filter=[".mp4"])
        self.logger.info(f"creating directory: {self._dest_dir.absolute()}")
        self._dest_dir.mkdir(parents=True, exist_ok=True)

        count = 0
        for file in cli.terminal.Progress(files):
            self.logger.debug(
                f"--moving {file.path.absolute()} -> {self._dest_dir / file.path.name}"
            )

            file.path.rename(self._dest_dir / file.path.name)
            count += 1  # lazy, just do the iterator once

        print(f"Moved {count} files to {self._dest_dir.absolute()}")


class StashJpeg(BaseCLI):
    """mini cli: copy .jp[e]g files into their own folder"""

    PROGNAME = __stash_jpeg__
    VERSION = __version__

    _dest_dir = pathlib.Path() / "JPEG"

    @cli.autoswitch(str, help="where to copy all mp4s")
    def dest_dir(self, dest_path=_dest_dir):
        self._dest_dir = pathlib.Path(dest_path)

    def main(self):
        self.logger.info("Hello World")

        files = tools.list_files(self._source_dir, file_filter=[".jpeg", ".jpg"])
        self.logger.info(f"creating directory: {self._dest_dir.absolute()}")
        self._dest_dir.mkdir(parents=True, exist_ok=True)

        count = 0
        for file in cli.terminal.Progress(files):
            self.logger.debug(
                f"--moving {file.path.absolute()} -> {self._dest_dir / file.path.name}"
            )

            file.path.rename(self._dest_dir / file.path.name)
            count += 1  # lazy, just do the iterator once

        print(f"Moved {count} files to {self._dest_dir.absolute()}")


class UnicornCLI(BaseCLI):
    """Plumbum Application"""

    PROGNAME = __cli_name__
    VERSION = __version__

    dest_dir = cli.SwitchAttr(
        "--dest-dir",
        str,
        default=pathlib.Path() / "PICKS",
        help='Destination to copy "keepers" to',
        envname="UNICORN_DEST_DIR",
    )

    stars = cli.SwitchAttr(
        "--stars",
        int,
        default=3,
        help='filter criteria: minimum stars to classify as "keepers"',
        envname="UNICORN_STARS",
    )

    nfs = cli.SwitchAttr(
        "--nfs",
        str,
        help="NFS destination to copy files to",
        envname="UNICORN_NFS",
    )

    smb = cli.SwitchAttr(
        "--smb",
        str,
        help="SMB destination to copy files to",
        envname="UNICORN_SMB",
    )

    def main(self):
        """main goes here"""
        self.logger.info("Hello World")


def run():
    """console entry_point"""
    UnicornCLI.run()


def run_stashvid():
    """console entry_point"""
    StashVideo.run()


def run_stashjpeg():
    """console entry_point"""
    StashJpeg.run()


if __name__ == "__main__":
    run()
