#!/usr/bin/env python

import plac
import sys
from bat import Bat
from pprint import pprint

ACTIONS = ['install', 'search', 'remove', 'update']
NOARG_ACTIONS = ['init', 'syncdb', 'remove_all', 'update_all', 'list_installed']
ACTIONS.extend(NOARG_ACTIONS)

def syncdb():
    bat = Bat()
    bat.syncdb()

def init():
    bat = Bat()
    bat.install_base()

def remove_all():
    bat = Bat()
    bat.remove_all()

def list_installed():
    print('Not implement yet!')

def install(*scripts):
    """install scripts"""
    if scripts.__len__() >= 1:
        for index in xrange(0, scripts.__len__()):
            bat = Bat(scripts[index])
            bat.install()
    else:
        print('Please use `vimpyre install <script-name>` and try again!')

def search(*scripts):
    """search script"""
    if scripts.__len__() > 1:
        print('Please search one script name!')
        sys.exit(1)

    bat = Bat(scripts[0])
    rets = bat.search()

    if rets:
        for item in rets:
            print('%s => %s' % (item['name'], item['description']))
    else:
        print('No vim-scripts found!')

def remove(*scripts):
    """remove scripts"""
    if scripts.__len__() >= 1:
        for index in xrange(0, scripts.__len__()):
            bat = Bat(scripts[index])
            bat.remove()
    else:
        print('Please use `vimpyre remove <script-name>` and try again!')


def update(*scripts):
    """update scripts"""
    if scripts.__len__() >= 1:
        for index in xrange(0, scripts.__len__()):
            bat = Bat(scripts[index])
            bat.update()
    else:
        print('Please use `vimpyre update <script-name>` and try again!')


@plac.annotations(
    action=', '.join(ACTIONS),
    scripts="vim-script")
def main(action, *scripts):
    """main function"""
    if action not in ACTIONS:
        print('no such action, exit!')
        sys.exit(1)

    if action not in NOARG_ACTIONS and not scripts:
        print('Please give a vim script name and try again!')
        sys.exit(1)
    elif action in NOARG_ACTIONS:
        eval(action + '()')
    else:
        eval(action + '("%s")' % scripts)


if __name__ == '__main__':
    plac.call(main)

