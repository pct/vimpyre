Vimpyre
=======

Vimpyre, Vim Scripts Manager (use pathogen, git, and python!)

Actions:
    init, install, search, remove, uninstall, update, browse, remove_all, uninstall_all, update_all, list_installed

Requirements
------------

1. git
2. python
3. python-plac (http://pypi.python.org/pypi/plac)
4. python-simplejson (http://pypi.python.org/pypi/simplejson)
5. python-requests (http://python-requests.org)

Install
-------
Use git or pip.

Use git::

    $ git clone git://github.com/pct/vimpyre.git
    $ cd vimpyre; sudo python setup.py install

Use pip::

    # pip install vimpyre

Usage
-----
- Init (get pathogen.vim and create ~/.vim/vimpyre)::

    $ vimpyre init
    ( Please add 'call pathogen#runtime_append_all_bundles("vimpyre")' to your .vimrc manually.)

- Search (Search vim-scripts from local repository)::

    $ vimpyre search html5
    $ vimpyre search othree/html5.vim

- Install (git clone vim-scripts to ~/.vim/vimpyre)::

    $ vimpyre install othree/html5.vim
    $ vimpyre install vim-scripts/html5.vim
    $ vimpyre install git://github.com/vim-scripts/ragtag.vim.git
    $ vimpyre install git://github.com/vim-scripts/ragtag.vim
    $ vimpyre install https://github.com/vim-scripts/ragtag.vim.git
    $ vimpyre install https://github.com/vim-scripts/ragtag.vim

- List Installed (list ~/.vim/vimpyre directories)::

    $ vimpyre list_installed

- Update (git pull)::

    $ vimpyre update html5.vim rails.vim

- Update All (git pull all repositories)::

    $ vimpyre update_all

- Remove (rm ~/.vim/vimpyre/<vim-scripts>)::

    $ vimpyre remove rails.vim html5.vim

- Remove All (rm ~/.vim/vimpyre*)::

    $ vimpyre remove_all
    (If you want to use vimpyre again, please `vimpyre init; vimpyre syncdb` first!)

- Browse (open script's homepage on vim.org)::

    $ vimpyre browse othree/html5.vim
    $ vimpyre browse https://github.com/othree/html5.vim

Todo
----

Please tell me what feature you want.

License
-------
http://www.opensource.org/licenses/bsd-license.php

The BSD 2-Clause License ("Simplified BSD License" or "FreeBSD License")::

    Copyright (c) 2011, pct(Jin-Sih, Lin)
    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

     * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
     * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Change Log
-----------

- Version 0.2.4

  * FIX: vimpyre init, vimpyre search result

- Version 0.2.3

  * FIX: Switched over to new GitHub API @ http://developer.github.com/v3/search for searching

- Version 0.2.2

    * FIX: `vimpyre browse`

- Version 0.2.1

    * FIX: setup.py requirements

- Version 0.2.0

    * FIX: `vimpyre search`, just use github search without using github API
    * REMOVE: `list_all`, `syncdb`
    * NEW: you could install github scripts with::

        $ vimpyre install othree/html5.vim
        $ vimpyre install vim-scripts/html5.vim
        $ vimpyre install git://github.com/vim-scripts/ragtag.vim.git
        $ vimpyre install git://github.com/vim-scripts/ragtag.vim
        $ vimpyre install https://github.com/vim-scripts/ragtag.vim.git
        $ vimpyre install https://github.com/vim-scripts/ragtag.vim

- Version 0.1.5

    * NEW: add `vimpyre browse <script_name>` to browse vim scripts page
    * CHANGE: vimpyre code refactoring


