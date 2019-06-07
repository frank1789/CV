CC    = xelatex
BB    = biber
FLAGS = -shell-escape -halt-on-error -interaction=batchmode
TEX   = $(wildcard *.tex)
BIB   = $(wildcard *.bib)

blue   = \033[0;34m
yellow = \033[0;33m
green  = \033[0;32m
end    = \033[0m

all: build clean

build:
	@echo "${blue}----------------------------------${end}"
	@echo "${blue}===== Build xelatex document =====${end}"
	@echo "${blue}----------------------------------${end}"
	@echo
	@echo "${yellow}compling... x1${end}"
	${CC} ${FLAGS} ${TEX}
	@echo "${yellow}compling... x2${end}"
	${CC} ${FLAGS} ${TEX}
	@echo "${yellow}compling... x3${end}"
	${CC} ${FLAGS} ${TEX}
	@echo "${green}Complete${end}"

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.out *.synctex.gz *.toc *.back
