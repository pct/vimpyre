#!/usr/bin/env python

from bat import Bat
from pprint import pprint

ACTIONS = ['install', 'search', 'remove', 'update', 'init']

def install(**scripts):
    """install scripts"""
    pass

def search(script):
    """search script"""
    pass

def remove(**scripts):
    """remove scripts"""
    pass

def update(**scripts):
    """update scripts"""
    pass

def init(scripts = 'pathogen.vim'):
    """
    vimpyre init,
    [1] add pathogen script
    [2] show pathogen messages
    """
    bat = Bat(scripts)
    bat.install_base()

def main(action, **scripts):
    """main function"""
    if action not in ACTIONS:
        import sys
        print('action not support, exit.')
        sys.exit(1)

    eval(action + '(%s)' % scripts)

if __name__ == '__main__':
    try:
        import plac
        plac.call(main)
    except ImportError:
        print('Please install python plac package')

