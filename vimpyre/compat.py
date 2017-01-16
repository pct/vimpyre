import sys

_ver = sys.version_info
is_py2 = (_ver[0] == 2)
is_py3 = (_ver[0] == 3)


if is_py2:
    from backports.shutil_get_terminal_size import get_terminal_size
elif is_py3:
    from shutil import get_terminal_size
