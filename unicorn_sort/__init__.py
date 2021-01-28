import pkgutil

__library_name__ = "unicorn_sort"
__version__ = pkgutil.get_data(__library_name__, "VERSION").decode("utf-8")
