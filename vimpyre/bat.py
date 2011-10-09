#!/usr/bin/env python
# coding: utf-8

import shutil
import sys
import urllib
from os import listdir, path, system

import simplejson

import util
from util import console

class Bat(object):

    CURR_SCRIPT = ''
    GITHUB_VIM_REPO = 'http://github.com/api/v2/json/repos/watched/vim-scripts'
    PATHOGEN_URL = 'http://github.com/vim-scripts/pathogen.vim/raw/master/plugin/pathogen.vim'
    VIM_PATH = path.join(path.expanduser('~'), '.vim')
    AUTOLOAD_PATH = path.join(VIM_PATH, 'autoload')
    VIMPYRE_PATH = path.join(VIM_PATH, 'vimpyre')
    VIMPYRE_DB_PATH = path.join(VIM_PATH, 'vimpyre.json')

    def __init__(self, script = ''):
        self.CURR_SCRIPT = script

    @property
    def bundles(self):
        """ List of bundles in the vimpyre path """
        try:
            with util.cd(self.VIMPYRE_PATH):
                return [item for item in listdir('.') if path.isdir(item)]
        except OSError:
            console('Cannot access your vimpyre path!')
            console('Please use `vimpyre init; vimpyre syncdb` first!')

    def install_base(self):
        """
        Install pathogen.vim and create vimpyre directory.

            >>> bat = Bat()
            >>> bat.install_base()
            => => Send a bat to catch pathogen.vim ...
            Catch done! Please add the following message to your .vimrc:
            call pathogen#runtime_append_all_bundles("vimpyre")
        """
        try:
            console('=> => Send a bat to catch pathogen.vim ...')
            raw_urlopen = urllib.urlopen(self.PATHOGEN_URL)
            if raw_urlopen.getcode() == 200:
                util.mkdir_p(self.AUTOLOAD_PATH)
                util.mkdir_p(self.VIMPYRE_PATH)
                raw_pathogen = raw_urlopen.read()
                pathogen = path.join(self.AUTOLOAD_PATH, 'pathogen.vim')
                with open(pathogen, 'w') as f:
                    f.write(raw_pathogen)
                console('Catch done! Please add the following to your .vimrc:')
                console('call pathogen#runtime_append_all_bundles("vimpyre")')
            else:
                console('Catch fail! Please try again!')
        except:
            console('[Unexpected Error] Catch fail! Please try again!')

    def syncdb(self):
        """
        Fetch http://github.com/api/v2/json/repos/show/vim-scripts

            >>> bat = Bat('')
            >>> bat.syncdb()
            => => Send a bat to sync vim-scripts repo ...
            Sync repo done!
        """
        try:
            console('=> => Send a bat to sync vim-scripts repo ...')
            raw_urlopen = urllib.urlopen(self.GITHUB_VIM_REPO)
            if raw_urlopen.getcode() == 200:
                raw_json = raw_urlopen.read()
                with open(self.VIMPYRE_DB_PATH, 'w') as f:
                    f.write(raw_json)
                console('Sync repo done!')
            else:
                console('Sync repo fail! Please try again!')
        except:
            console('[Unexpected Error] Sync repo fail! Please try again')

    def install(self):
        console('=> => Send a bat to catch %s' % self.CURR_SCRIPT)
        try:
            ret = self._check_name()
            if ret:
                cmd_fetch = 'git clone --depth 1 %s' % (ret['url'] + '.git')
                util.mkdir_p(self.VIMPYRE_PATH)
                with util.cd(self.VIMPYRE_PATH):
                    system(cmd_fetch)
            else:
                msg = ('%s not found! Please use `vimpyre search <vim-script>`'
                       ' to check the script name and install again!' %
                       self.CURR_SCRIPT)
                console(msg)
        except:
            self.install_base()
            self.syncdb()

    def update(self):
        console('=> => Send a bat to update %s' % self.CURR_SCRIPT)
        bundle_path = path.join(self.VIMPYRE_PATH, self.CURR_SCRIPT)
        if path.isdir(bundle_path):
            with util.cd(bundle_path):
                system('git pull')
            console('%s update done!' % self.CURR_SCRIPT)
        else:
            console('%s does not exist!' % self.CURR_SCRIPT)

    def update_all(self):
        console('=> => Send bats to update all installed vim-scripts ...')
        if not self.bundles:
            console('No vim-scripts! Please use `vimpyre install <vim-scripts>` first!')
            sys.exit(1)

        for item in self.bundles:
            console('=> Update %s ...' % item)
            with util.cd(path.join(self.VIMPYRE_PATH, item)):
                system('git pull')
        console('Update all vim-scripts done!')

    def remove(self):
        console('=> => Send a bat to bite %s' % self.CURR_SCRIPT)
        bundle_path = path.join(self.VIMPYRE_PATH, self.CURR_SCRIPT)
        if self._check_name() and path.isdir(bundle_path):
            shutil.rmtree(bundle_path)
            console('%s removed!' % self.CURR_SCRIPT)
        else:
            console('%s does not exist!' % self.CURR_SCRIPT)

    def remove_all(self):
        console('=> => Send bats to clean all vimpyre files')
        try:
            with util.cd(self.VIMPYRE_PATH):
                for bundle in self.bundles:
                    shutil.rmtree(bundle)
            console('Remove vimpyre bundles done!')
        except OSError:
            console('Could not remove bundles! Please verify permissions of '
                    'your bundle directories.')
        else:
            console('Please remove %s/pathogen.vim manually and clean `call pathogen#runtime_append_all_bundles("vimpyre")` from your .vimrc!' % self.AUTOLOAD_PATH)
            console('')
            console('If you wish to use vimpyre to manage your vim scripts again, you need to use `vimpyre init; vimpyre syncdb` first!')

    def list_installed(self):
        console('=> => Send bats to collect all your vim-scripts')
        if not self.bundles:
            console('No vim-scripts found!')
            sys.exit(1)

        db = self._load_db()
        for bundle in self.bundles:
            found = False
            for repo in db['repositories']:
                if bundle == repo['name']:
                    console('\033[1m%s\033[m => %s' % (repo['name'].encode('utf-8'), repo['description'].encode('utf-8')))
                    found = True
                    break

            if not found:
                console('\033[1m%s\033[m' % bundle.encode('utf-8'))

    def _load_db(self):
        """ Loads vim-scripts repository data from GitHub JSON """
        try:
            db = simplejson.loads(open(self.VIMPYRE_DB_PATH,'r').read())
            assert 'repositories' in db
            return db
        except (IOError, simplejson.JSONDecodeError, AssertionError):
            console('Missing or invalid vimpyre script database -- please run `vimpyre syncdb`!')
            sys.exit(1)

    def _check_name(self):
        try:
            search_ret = self.search()
            rets = [item for item in search_ret if self.CURR_SCRIPT == item['name']]
            if rets:
                return rets[0]
            return []
        except:
            pass

    def list_all(self):
        db = self._load_db()
        for item in db['repositories']:
            if path.isdir(path.join(self.VIMPYRE_PATH, item['name'])):
                console('%s => %s [installed]' % (item['name'].encode('utf-8'), item['description'].encode('utf-8')))
            else:
                console('%s => %s' % (item['name'].encode('utf-8'), item['description'].encode('utf-8')))

    def search(self):
        """
        Search github vim-scripts, return array.

            >>> bat = Bat('xxxxxxxx')
            >>> bat.search()
            []
            >>> bat = Bat('pathogen')
            >>> bat.search() # doctest: +ELLIPSIS
            [{..., 'name': 'pathogen.vim'}]
        """
        db = self._load_db()
        return [item for item in db['repositories']
                if self.CURR_SCRIPT.lower() in item['name'].lower()
                or self.CURR_SCRIPT.lower() in item['description'].lower()]

