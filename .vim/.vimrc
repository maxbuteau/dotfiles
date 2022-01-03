syntax on

set noerrorbells
set exrc
set hidden
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set number relativenumber
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set scrolloff=8
set termguicolors
set completeopt=menuone,noinsert,noselect
" set colorcolumn=140
set signcolumn=yes
" highligh ColorColumn ctermbg=0 guibg=lightgrey   
set updatetime=50

call plug#begin('~/.vim/plugged')

" Colorscheme
Plug 'morhetz/gruvbox'
" search tool that recursively searches through current directory
Plug 'jremmen/vim-ripgrep'
Plug 'tpope/vim-fugitive'
Plug 'vim-utils/vim-man'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'ycm-core/YouCompleteMe', { 'do': './install.py' }
Plug 'mbbill/undotree'
Plug 'vim-airline/vim-airline'
" Plug 'prettier/vim-prettier', {'do': 'npm install'}

call plug#end()

colorscheme gruvbox
set background=dark

" Allows ripgrep to always detect your root
if executable('rg')
    let g:rg_derive_root='true'
endif

let g:ctrlp_user_command = ['.git/', 'git --git-dir=%s/.git ls-files -oc --exclude-standard']
let mapleader = " "
let g:netrw_browse_split = 2
let g:netrw_winsize = 25

let g:ctrlp_use_caching = 0

" Resize window
nnoremap <silent> <Leader>= :vertical resize +5<CR>
nnoremap <silent> <Leader>- :vertical resize -5<CR>

" Switch windows
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>
" Open undotree
nnoremap <leader>u :UndotreeShow<CR>
" Open netrw in a small window
nnoremap <leader>pv :wincmd v<bar> :Ex <bar> :vertical resize 30<CR>
" Project search with ripgrep
nnoremap <leader>ps :Rg<SPACE>
" Go to definition
nnoremap <silent> <Leader>gd :YcmCompleter GoTo<CR>
" Fix error automatically
nnoremap <silent> <Leader>gf :YcmCompleter FixIt<CR>

inoremap jk <Esc>
inoremap kj <Esc>

augroup MAXIME
    autocmd!
    autocmd BufRead,BufNewFile *.vue setfiletype html
augroup END
