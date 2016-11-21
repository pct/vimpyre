#!/usr/bin/env python
# coding: utf-8

import shutil
import sys
import urllib
import webbrowser
import subprocess
from os import listdir, path, system, environ


import simplejson

from vimpyre import util
from vimpyre.util import console
from vimpyre.github import GitHub

class Bat(object):

    CURR_SCRIPT = ''
    VIM_PATH = path.join(path.expanduser('~'), '.vim')
    AUTOLOAD_PATH = path.join(VIM_PATH, 'autoload')
    VIMPYRE_PATH = path.join(VIM_PATH, 'vimpyre')
    
    @property
    def pathogen_url(self):
        try:
            return environ['VIM_PATHOGEN_URL']
        except:
            return 'https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim'

    def __init__(self, script = ''):
        self.CURR_SCRIPT = script
        self.github = GitHub()

    def _check_name(self):
        if self.CURR_SCRIPT.startswith('http') or self.CURR_SCRIPT.startswith('git'):
            return self.CURR_SCRIPT

        try:
            search_ret = self.search()
            rets = [item for item in search_ret if self.CURR_SCRIPT == item['name']]
            if rets:
                rets[0]['homepage'] = 'https://github.com/' + self.CURR_SCRIPT
                return rets[0]
            return []
        except:
            pass

    def _filter_script_name(self):
        return self.CURR_SCRIPT.split('/')[-1]

    def _render_fetch_url(self, ret):
        if type(ret) == dict:
            fetch_url = ret['url'] + '.git'
        else:
            fetch_url = ret

        return fetch_url

    @property
    def bundles(self):
        """ List of bundles in the vimpyre path """
        try:
            with util.cd(self.VIMPYRE_PATH):
                return [item for item in listdir('.') if path.isdir(item)]
        except OSError:
            console('Cannot access your vimpyre path!')

    def install_base(self):
        """
        Install pathogen.vim and create vimpyre directory.

            >>> bat = Bat()
            >>> bat.install_base()
            => => Send a bat to catch pathogen.vim ...
            Catch done! Please add the following message to your .vimrc:
            execute pathogen#infect('bundle/{}', 'vimpyre/{}')
        """
        try:
            console('=> => Send a bat to catch pathogen.vim ...')
            raw_urlopen = urllib.urlopen(self.pathogen_url)
            if raw_urlopen.getcode() == 200:
                util.mkdir_p(self.AUTOLOAD_PATH)
                util.mkdir_p(self.VIMPYRE_PATH)
                raw_pathogen = raw_urlopen.read()
                pathogen = path.join(self.AUTOLOAD_PATH, 'pathogen.vim')
                with open(pathogen, 'w') as f:
                    f.write(raw_pathogen)
                console('Catch done! Please add the following to your .vimrc:')
                console("execute pathogen#infect('bundle/{}', 'vimpyre/{}')")
            else:
                console('Pathogen vimscript not found in %s' % self.pathogen_url)
                console('You can change this url with enviroment variable VIM_PATHOGEN_URL')
                console('Catch fail! Please try again!')
        except:
            console('[Unexpected Error] Catch fail! Please try again!')

    def install(self):
        console('=> => Send a bat to catch %s' % self.CURR_SCRIPT)

        try:
            ret = self._check_name()
            if ret:
                fetch_url = self._render_fetch_url(ret)
                cmd_fetch = 'git clone --depth 1 %s' % fetch_url
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

    def update(self):
        console('=> => Send a bat to update %s' % self.CURR_SCRIPT)
        bundle_path = path.join(self.VIMPYRE_PATH, self._filter_script_name())
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
        bundle_path = path.join(self.VIMPYRE_PATH, self._filter_script_name())
        if path.isdir(bundle_path):
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
            console('Please remove %s/pathogen.vim manually!' % self.AUTOLOAD_PATH)
            console('')
            console('If you wish to use vimpyre to manage your vim scripts again, you need to use `vimpyre init` first!')

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

        rets = self.github.search(self.CURR_SCRIPT)

        return [item for item in rets
                if self.CURR_SCRIPT.lower() in item['name'].lower()
                or self.CURR_SCRIPT.lower() in item['description'].lower()]

    def open_homepage(self):
        console('=> => Send bats to open your browser...')
        bundle = self._check_name()
        if type(bundle) == dict and bundle['homepage']:
            webbrowser.open(bundle['homepage'])
        elif bundle:
            webbrowser.open(bundle)
        else:
            console('Sorry, no homepage found for this script.')

    def list_installed(self):
        console('=> => Send bats to collect all your vim-scripts')
        if not self.bundles:
            console('No vim-scripts found!')
            sys.exit(1)

        for bundle in self.bundles:
            bundle_path = path.join(self.VIMPYRE_PATH, bundle)
            with util.cd(bundle_path):
                if path.isfile(path.join('.git', 'config')):
                    url = subprocess.check_output(['grep', 'url', '.git/config']).decode("utf-8")
                    url = url.replace('\turl = ', '').replace('\n', '')
                    console('\033[1m%s\033[m => %s' % (bundle, url))
                else:
                    console('\033[0;31m%s\033[m => %s' % (bundle, 'No git repository!'))
