"""main CLI"""

import pathlib
import logging

from plumbum import cli

from . import __version__

__cli_name__ = "unicorn"


class UnicornCLI(cli.Application):
    """Plumbum Application"""

    PROGNAME = __cli_name__
    VERSION = __version__

    source_dir = cli.SwitchAttr(
        "--source-dir",
        str,
        default=pathlib.Path(),
        help="Folder full of images CR2/CR3/JPEG",
        envname="UNICORN_SOURCE_DIR",
    )

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
        logging.info("Hello World")


def run():
    """console entry_point"""
    UnicornCLI.run()


if __name__ == "__main__":
    run()
