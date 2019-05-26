CC = xelatex
BB = biber
FLAGS = -shell-escape
TEX = $(wildcard *.tex)
BIB = $(wildcard *.bib)

all: build clean

build:
	@echo "----------------------------------"
	@echo "===== Build xelatex document ====="
	@echo "----------------------------------"
	${CC} ${FLAGS} ${TEX}

clean:
	rm -rf *.aux *.fdb_latexmk *.fls *.log *.out *.synctex.gz *.toc *.back
