#!/usr/bin/env python
# coding: utf-8

import os
import sys
import plac
from bat import Bat

VIM_PATH = os.path.expanduser('~')+'/.vim/'
ACTIONS = ['install', 'search', 'remove', 'update']
NOARG_ACTIONS = ['init', 'syncdb', 'remove_all', 'update_all', 'list_installed', 'list_all']
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

def update_all():
    bat = Bat()
    bat.update_all()

def list_installed():
    bat = Bat()
    bat.list_installed()

def list_all():
    bat = Bat()
    bat.list_all()

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

    print('=> => Send bats to search vim-scripts ...')
    if rets:
        for item in rets:
            if os.path.exists(VIM_PATH + 'vimpyre/%s' % item['name']):
                print('\033[1m%s\033[m => %s \033[1m[installed]\033[m' % (item['name'].encode('utf-8'), item['description'].encode('utf-8')))
            else:
                print('\033[1m%s\033[m => %s' % (item['name'].encode('utf-8'), item['description'].encode('utf-8')))
    else:
        print('No such vim-scripts! Please use `vimpyre syncdb` and try again!')

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
    scripts="vim-script1, vim-script2, ...")
def dispatch(action, *scripts):
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
        scripts = '"' + '", "'.join(scripts) + '"'
        eval(action + '(%s)' % scripts)

def main():
    plac.call(dispatch)

if __name__ == '__main__':
    main()

