CC = xelatex
BB = biber
FLAGS = -shell-escape
TEX = $(wildcard *.tex)
BIB = $(wildcard *.bib)

all: build

build:
	@echo "Build xelatex document"
	${CC} ${FLAGS} ${TEX}
	@echo "clean temporally files"
	make clean

clean:
	rm *.aux *.fdb_latexmk *.fls *.log *.out *.synctex.gz *.toc *.back
