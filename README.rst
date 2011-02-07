=======
Vimpyre
=======

Vimpyre, Vim Scripts Manager (use pathogen, git, and python!)

Actions:
    init, syncdb, install, search, remove, update, remove_all, update_all, list_installed, list_all

------------
Requirements
------------

1. git
2. pyhton
3. python-lxml (http://codespeak.net/lxml/)
4. python-plac (http://pypi.python.org/pypi/plac)
5. python-simplejson (http://pypi.python.org/pypi/simplejson)

-------
Install
-------
Step::

    $ git clone git://github.com/pct/vimpyre.git
    $ cd vimpyre; sudo python setup.py install

------
Usage
------
- Init (get pathogen.vim and create ~/.vim/vimpyre)::

    $ vimpyre init
    ( Please add 'call pathogen#runtime_append_all_bundles("vimpyre")' to your .vimrc manually.)

- SyncDB (get github vim-scripts repository)::

    $ vimpyre syncdb

- Search (Search vim-scripts from local repository)::

    $ vimpyre search html5.vim

- Install (git clone vim-scripts to ~/.vim/vimpyre)::

    $ vimpyre install html5.vim rails.vim calendar.vim

- List Installed (list ~/.vim/vimpyre directories)::

    $ vimpyre list_installed

- List All Scripts (list ~/.vim/vimpyre.json)::

    $ vimpyre list_all

- Update (git pull)::

    $ vimpyre update html5.vim rails.vim

- Update All (git pull all repositories)::

    $ vimpyre update_all

- Remove (rm ~/.vim/vimpyre/<vim-scripts>)::

    $ vimpyre remove rails.vim html5.vim

- Remove All (rm ~/.vim/vimpyre*)::

    $ vimpyre remove_all
    (If you want to use vimpyre again, please `vimpyre init; vimpyre syncdb` first!)

---------------
Current Status
---------------

Version 0.1.3

