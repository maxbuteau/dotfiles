source ~/.config/nvim/sets.vim

call plug#begin('~/.vim/plugged')

" Colorschemes
Plug 'morhetz/gruvbox'
Plug 'dracula/vim', {'as':'dracula'}
" search tool that recursively searches through current directory
Plug 'jremmen/vim-ripgrep'
" Plug 'tpope/vim-fugitive'
Plug 'vim-utils/vim-man'
" Plug 'ctrlpvim/ctrlp.vim'
" Plug 'ycm-core/YouCompleteMe', { 'do': './install.py' }
Plug 'mbbill/undotree'
Plug 'vim-airline/vim-airline'
" Plug 'prettier/vim-prettier', {'do': 'npm install'}
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'posva/vim-vue'
Plug 'pangloss/vim-javascript'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'cakebaker/scss-syntax.vim'
Plug 'lervag/vimtex'
" python syntax highlighting
Plug 'vim-python/python-syntax'

call plug#end()

colorscheme gruvbox
set background=dark
""colorscheme dracula

"set pyxversion=3
" Allows ripgrep to always detect your root
if executable('rg')
    let g:rg_derive_root='true'
endif

let g:python_highlight_all = 1
let g:python_highlight_space_errors = 0

" let g:ctrlp_user_command = ['.git/', 'git --git-dir=%s/.git ls-files -oc --exclude-standard']
let mapleader = " "
let g:netrw_browse_split = 2
let g:netrw_winsize = 25

""let g:tex_flavor = 'latex'
let g:vimtex_indent_enabled = 'true'
""let g:vimtex_syntax_enabled = 0

" let g:ctrlp_use_caching = 0
" let g:coc_node_path = '/home/mbuteau/.nvm/versions/node/v14.21.3/bin/node'

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
nnoremap <silent> gd <Plug>(coc-definition)
nnoremap <silent> gy <Plug>(coc-type-definition)
nnoremap <silent> gi <Plug>(coc-implementation)
nnoremap <silent> gr <Plug>(coc-references)

" Fzf remap
" fzf file fuzzy search that respects .gitignore
" If in git directory, show only files that are committed, staged, or unstaged
" else use regular :Files
nnoremap <expr> <leader>f (len(system('git rev-parse')) ? ':Files' : ':GFiles --exclude-standard --others --cached')."\<cr>"

inoremap jk <Esc>
inoremap kj <Esc>

" Add undo break points
inoremap , ,<c-g>u
inoremap . .<c-g>u
inoremap ! !<c-g>u
inoremap ? ?<c-g>u
" Make Y behave like C and D
nnoremap Y y$


" Toggle spellcheck
nnoremap <leader>o :setlocal spell! spelllang=en_us<CR>

" Vertical jumps bigger than 5 added to jumplist
nnoremap <expr> k (v:count > 5 ? "m'" . v:count : "") . 'k'
nnoremap <expr> j (v:count > 5 ? "m'" . v:count : "") . 'j'

" Use tab for trigger completion with characters ahead and navigate
" NOTE: There's always complete item selected by default, you may want to enable
" no select by `"suggest.noselect": true` in your configuration file
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config
inoremap <silent><expr> <TAB>
      \ coc#pum#visible() ? coc#pum#next(1) :
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()

inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"

" Make <CR> to accept selected completion item or notify coc.nvim to format
" <C-g>u breaks current undo, please make your own choice
inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

function! CheckBackspace() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction





"" use <tab> for trigger completion and navigate to the next complete item
"function! s:check_back_space() abort
"  let col = col('.') - 1
"  return !col || getline('.')[col - 1]  =~ '\s'
"endfunction
"
"inoremap <silent><expr> <Tab>
"      \ pumvisible() ? "\<C-n>" :
"      \ <SID>check_back_space() ? "\<Tab>" :
"      \ coc#refresh()

augroup MAXIME
    autocmd!
    autocmd BufRead,BufNewFile *.vue setfiletype html
    autocmd BufWritePost *.tex silent! execute "!pdflatex % >/dev/null 2>&1" | redraw!
augroup END
