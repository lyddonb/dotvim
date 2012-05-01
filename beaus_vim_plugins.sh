#!/bin/bash

#hg clone https://bitbucket.org/sjl/dotfiles
echo Loading Bundles from Git
git submodule add http://github.com/tpope/vim-fugitive.git bundle/fugitive
git submodule add https://github.com/msanders/snipmate.vim.git bundle/snipmate
git submodule add https://github.com/tpope/vim-surround.git bundle/surround
git submodule add https://github.com/tpope/vim-git.git bundle/git
git submodule add https://github.com/ervandew/supertab.git bundle/supertab
git submodule add https://github.com/fholgado/minibufexpl.vim.git bundle/minibufexpl
git submodule add https://github.com/mitechie/pyflakes-pathogen.git bundle/pyflakes
#git submodule add https://github.com/mileszs/ack.vim.git bundle/ack
git submodule add https://github.com/sjl/gundo.vim.git bundle/gundo
git submodule add https://github.com/fs111/pydoc.vim.git bundle/pydoc
git submodule add https://github.com/vim-scripts/pep8.git bundle/pep8
git submodule add https://github.com/alfredodeza/pytest.vim.git bundle/py.test
git submodule add https://github.com/reinh/vim-makegreen bundle/makegreen
git submodule add https://github.com/vim-scripts/TaskList.vim.git bundle/tasklist
git submodule add https://github.com/vim-scripts/The-NERD-tree.git bundle/nerdtree
git submodule add https://github.com/scrooloose/nerdcommenter.git bundle/nerdcommenter
git submodule add https://github.com/sontek/rope-vim.git bundle/ropevim
git submodule add https://github.com/scrooloose/syntastic.git bundle/syntastic
git submodule add https://github.com/majutsushi/tagbar.git bundle/tagbar
git submodule add https://github.com/vim-scripts/Jinja bundle/jinja
git submodule add https://github.com/Townk/vim-autoclose bundle/autoclose
git submodule add https://github.com/Lokaltog/vim-easymotion bundle/vim-easymotion
git submodule add https://github.com/jceb/vim-orgmode bundle/vim-orgmode
git submodule add https://github.com/vim-scripts/Rainbow-Parenthesis bundle/rainbow
git submodule add https://github.com/duff/vim-scratch bundle/scratch
git submodule add https://github.com/sjl/threesome.vim bundle/threesome
git submodule add https://github.com/vim-scripts/YankRing.vim bundle/yankfing
git submodule add https://github.com/robgleeson/hammer.vim bundle/hammer
git submodule add https://github.com/michaeljsmith/vim-indent-object bundle/indent-object
git submodule add https://github.com/lambdalisue/nose.vim bundle/nosecompiler
git submodule add https://github.com/sjl/strftimedammit.vim bundle/strftimedammit
git submodule add https://github.com/kchmck/vim-coffee-script bundle/vim-coffee-script
git submodule add https://github.com/pangloss/vim-javascript bundle/vim-javascript
git submodule add https://github.com/kien/ctrlp.vim bundle/ctrlp.vim
git submodule add https://github.com/benmills/vimux bundle/vimux
git submodule add https://github.com/sjl/vitality.vim bundle/vitality
echo Done loading bundles
git submodule init
git submodule update
echo Updating...
git submodule foreach git submodule init
git submodule foreach git submodule update
echo Complete
