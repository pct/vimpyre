#!/usr/bin/env python
# coding: utf-8

import sys
import plac
from os import path

from bat import Bat
from util import console

VIM_PATH = path.join(path.expanduser('~'), '.vim')
ACTIONS = ['install', 'search', 'remove', 'uninstall', 'update', 'browse']
NOARG_ACTIONS = ['init', 'remove_all', 'uninstall_all', 'update_all', 'list_installed']
ACTIONS.extend(NOARG_ACTIONS)

def init():
    bat = Bat()
    bat.install_base()

def remove_all():
    bat = Bat()
    bat.remove_all()

def uninstall_all():
    remove_all()

def update_all():
    bat = Bat()
    bat.update_all()

def list_installed():
    bat = Bat()
    bat.list_installed()

def install(*scripts):
    """install scripts"""
    if len(scripts) >= 1:
        for index in xrange(0, len(scripts)):
            bat = Bat(scripts[index])
            bat.install()
    else:
        console('Please use `vimpyre install <script-name>` and try again!')

def search(*scripts):
    """search script"""
    if len(scripts) > 1:
        console('Please search one script name!')
        sys.exit(1)

    bat = Bat(scripts[0])
    rets = bat.search()

    console('=> => Send bats to search vim-scripts ...')
    if rets:
        for item in rets:
            if path.isdir(path.join(VIM_PATH, 'vimpyre', item['name'])):
                console('\033[1m%s\033[m => %s \033[1m[installed]\033[m' % (item['name'].encode('utf-8'), item['description'].encode('utf-8')))
            else:
                console('\033[1m%s\033[m => %s | last: %s' % (item['name'].encode('utf-8'), item['description'].encode('utf-8'), item['updated_at']))
    else:
        console('No such vim-scripts!')

def remove(*scripts):
    """remove scripts"""
    if len(scripts) >= 1:
        for index in xrange(0, len(scripts)):
            bat = Bat(scripts[index])
            bat.remove()
    else:
        console('Please use `vimpyre remove <script-name>` and try again!')

def uninstall(*scripts):
    remove(*scripts)

def update(*scripts):
    """update scripts"""
    if len(scripts) >= 1:
        for index in xrange(0, len(scripts)):
            bat = Bat(scripts[index])
            bat.update()
    else:
        console('Please use `vimpyre update <script-name>` and try again!')

def browse(*scripts):
    """browse script's homepage in your web browser"""
    if len(scripts) >= 1:
        for index in xrange(0, len(scripts)):
            bat = Bat(scripts[index])
            bat.open_homepage()
    else:
        console('Please use `vimpyre browse <script-name>` and try again!')


@plac.annotations(
    action=', '.join(ACTIONS),
    scripts="vim-script1, vim-script2, ...")
def dispatch(action, *scripts):
    """main function"""
    if action not in ACTIONS:
        console('no such action, exit!')
        sys.exit(1)

    if action not in NOARG_ACTIONS and not scripts:
        console('Please give a vim script name and try again!')
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

