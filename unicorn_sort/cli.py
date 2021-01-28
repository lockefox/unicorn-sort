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

    def main(self):
        """main goes here"""
        logging.info("Hello World")


def run():
    """console entry_point"""
    UnicornCLI.run()


if __name__ == "__main__":
    run()
