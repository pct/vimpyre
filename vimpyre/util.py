#!/usr/bin/env python
#coding=utf-8

import errno
import os
from contextlib import contextmanager

def mkdir_p(path):
    """Create nested directories, not complaining if they exist"""
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            pass
        else: raise


@contextmanager
def cd(dir):
    """Context manager to change directory for the duration of a block

    Example::

        with cd(os.path.expanduser('~')):
            # ...code operting in home directory...

        # ...back to operating in process' original directory...

    """
    original_dir = os.getcwd()
    try:
        os.chdir(dir)
        yield dir
    finally:
        os.chdir(original_dir)

