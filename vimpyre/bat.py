#!/usr/bin/env python

import os
import urllib
import lxml.html as lhtml
import simplejson

class Bat(object):

    CURR_SCRIPT = ''
    GITHUB_VIM_URL = 'http://vim-scripts.github.com/'
    GITHUB_VIM_REPO = 'http://github.com/api/v2/json/repos/show/vim-scripts'
    PATHOGEN_URL = 'http://github.com/vim-scripts/pathogen.vim/raw/master/plugin/pathogen.vim'
    VIM_PATH = os.path.expanduser('~')+'/.vim/'
    AUTOLOAD_PATH = VIM_PATH + 'autoload'
    VIMPYRE_PATH = VIM_PATH + 'vimpyre'
    VIMPYRE_DB_PATH = VIM_PATH + 'vimpyre.json'

    def __init__(self, script = ''):
        self.CURR_SCRIPT = script

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
            print('=> => Send a bat to catch pathogen.vim ...')
            cmd_create_autoload_dir = 'mkdir -p %s' % self.AUTOLOAD_PATH
            cmd_create_vimpyre_dir = 'mkdir -p %s' % self.VIMPYRE_PATH
            raw_urlopen = urllib.urlopen(self.PATHOGEN_URL)
            if raw_urlopen.getcode() == 200:
                raw_pathogen = raw_urlopen.read()
                os.system(cmd_create_autoload_dir)
                os.system(cmd_create_vimpyre_dir)
                f = open(self.AUTOLOAD_PATH + '/pathogen.vim', 'w')
                f.write(raw_pathogen)
                f.close()
                print('Catch done! Please add the following message to your .vimrc:')
                print('call pathogen#runtime_append_all_bundles("vimpyre")')
            else:
                print('Catch fail! Please try again!')
        except:
            print('[Unexpected Error] Catch fail! Please try again!')

    def syncdb(self):
        """
        Fetch http://github.com/api/v2/json/repos/show/vim-scripts

            >>> bat = Bat('')
            >>> bat.syncdb()
            => => Send a bat to sync vim-scripts repo ...
            Sync repo done!
        """
        try:
            print('=> => Send a bat to sync vim-scripts repo ...')
            raw_urlopen = urllib.urlopen(self.GITHUB_VIM_REPO)
            if raw_urlopen.getcode() == 200:
                raw_json = raw_urlopen.read()
                f = open(self.VIMPYRE_DB_PATH, 'w')
                f.write(raw_json)
                f.close()
                print('Sync repo done!')
            else:
                print('Sync repo fail! Please try again!')
        except:
            print('[Unexpected Error] Sync repo fail! Please try again')

    def install(self):
        print('=> => Send a bat to catch %s' % self.CURR_SCRIPT)
        try:
            ret = self._check_name()
            if ret:
                os.system('mkdir -p %s' % self.VIMPYRE_PATH)
                cmd_fetch = 'cd %s; git clone %s' % (self.VIMPYRE_PATH, ret['url'].replace('http://', 'git://'))
                os.system(cmd_fetch)
            else:
                print('%s not found! Please use `vimpyre search <vim-script>` to check the script name and install again!' % self.CURR_SCRIPT)
        except:
            self.install_base()
            self.syncdb()

    def update(self):
        print('=> => Send a bat to update %s' % self.CURR_SCRIPT)
        if os.path.exists('%s/%s' % (self.VIMPYRE_PATH, self.CURR_SCRIPT)):
            os.system('cd %s/%s; git pull' % (self.VIMPYRE_PATH, self.CURR_SCRIPT))
            print('%s update done!' % self.CURR_SCRIPT)
        else:
            print('%s not exist!' % self.CURR_SCRIPT)

    def update_all(self):
        print('=> => Send bats to update all installed vim-scripts ...')
        try: 
            rets = os.listdir(self.VIMPYRE_PATH)
            if rets:
                for item in rets:
                    print('=> Update %s ...' % item)
                    os.system('cd %s/%s; git pull' % (self.VIMPYRE_PATH, item))
                print('Update all vim-scripts done!')
            else:
                print('No vim-scripts! Please use `vimpyre install <vim-scripts>` first!')
        except OSError:
            print('Cannot access your vimpyre path!\nPlease use `vimpyre init; vimpyre syncdb; vimpyre install <vim-scripts>` first!')
        except:
            print('[Unexpected Error] Please try again!')

    def remove(self):
        print('=> => Send a bat to bite %s' % self.CURR_SCRIPT)
        cmd_remove = 'cd %s; rm -rf %s' % (self.VIMPYRE_PATH, self.CURR_SCRIPT)
        if self._check_name() and os.path.exists('%s/%s' % (self.VIMPYRE_PATH, self.CURR_SCRIPT)):
            os.system(cmd_remove)
            print('%s removed!' % self.CURR_SCRIPT)
        else:
            print('%s not exists!' % self.CURR_SCRIPT)
    
    def remove_all(self):
        print('=> => Send bats to clean all vimpyre files')
        if os.path.exists(self.VIMPYRE_PATH):
            cmd_remove_all = 'rm -rf %s*' % self.VIMPYRE_PATH
            os.system(cmd_remove_all)
            print('Remove vimpyre bundles done!')
        print('Please remove %s/pathogen.vim manually and clean `call pathogen#runtime_append_all_bundles("vimpyre")` from your .vimrc!' % self.AUTOLOAD_PATH)
        print('If you still want to use vimpyre to manage your vim scripts, you have to use `vimpyre init; vimpyre syncdb` first!')
    
    def list_installed(self):
        print('=> => Send bats to collect all your vim-scripts')
        if os.path.exists(self.VIMPYRE_PATH):
            rets = os.listdir(self.VIMPYRE_PATH)
            if rets:
                try:
                    repo = simplejson.loads(open(self.VIMPYRE_DB_PATH,'r').read())
                    db_items = repo['repositories']
                    for item in rets:
                        for db_item in db_items:
                            if item == db_item['name']:
                                print('\033[1m%s\033[m => %s' % (db_item['name'], db_item['description']))
                                found = True
                                break
                            else:
                                found = False

                        if not found:
                            print('\033[1m%s\033[m' % item)
                except:
                    print('Please use `vimpyre init; vimpyre syncdb; vimpyre install <vim-scripts>` first!')
            else:
                print('No vim-scripts found!')
        else:
            print('Please use `vimpyre init; vimpyre syncdb; vimpyre install <vim-scripts>` first!')

    def _check_name(self):
        try:
            search_ret = self.search()
            rets = [item for item in search_ret if self.CURR_SCRIPT == item['name']]
            if rets:
                return rets[0]
            return []
        except:
            pass

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
        try:
            repo = simplejson.loads(open(self.VIMPYRE_DB_PATH,'r').read())
            db_items = repo['repositories']
            if db_items:
                return [item for item in db_items if self.CURR_SCRIPT in item['name'] or self.CURR_SCRIPT in item['description']]
        except:
            pass
