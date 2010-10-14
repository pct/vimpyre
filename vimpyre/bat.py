#!/usr/bin/env python

import os
import urllib
import lxml.html as lhtml
from pprint import pprint

class Bat(object):

    CURR_SCRIPT = ''
    GITHUB_VIM_URL = 'http://vim-scripts.github.com/'
    PATHOGEN_URL = 'http://github.com/vim-scripts/pathogen.vim/raw/master/plugin/pathogen.vim'
    PLUGIN_PATH = os.path.expanduser('~')+'/.vim/autoload'

    def __init__(self, script):
        self.CURR_SCRIPT = script

    def install_base(self):
        """ install pathogen.vim """
        try:
            print('Send a bat to catch pathogen.vim ...')
            cmd_create_dir = 'mkdir -p %s' % self.PLUGIN_PATH
            raw_urlopen = urllib.urlopen(self.PATHOGEN_URL)
            if raw_urlopen.getcode() == 200:
                raw_pathogen = raw_urlopen.read()
                os.system(cmd_create_dir)
                f = open(self.PLUGIN_PATH + '/pathogen.vim', 'w')
                f.write(raw_pathogen)
                f.close()
                print('Catch done! Please add the following message to your .vimrc:')
                print('call pathogen#runtime_append_all_bundles("vimpyre")')
            else:
                print('Catch fail! Please try again!')
        except:
            print('Catch fail! Please try again!')

    def git_fetch(self):
        """git clone"""
        pass

    def git_update(self):
        """git pull"""
        pass

    def parse_github(self):
        script_url = self.GITHUB_BASEURL + self.CURR_SCRIPT

    def search_github(self):
        """ return item (name, desc, github url) """
        rets = lhtml.parse(self.GITHUB_VIM_URL).xpath('//a[contains(".,%s")]' % self.CURR_SCRIPT)

        if rets:
            items = []
            item = {'name': '', 'desc': '', 'giturl': ''}
            for ret in rets:
                item['name'] = ret.text.strip()
                item['desc'] = ret.xpath('.//parent::td')[0].text_content().strip()
                item['giturl'] = ret.xpath('.//@href')[0].strip()
                items.append(item)

            return items

        return False


    def install(self):
        pass

