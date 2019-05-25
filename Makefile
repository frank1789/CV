all: build run

build:
    latexmk -xelatex -synctex=1 main.tex

clean:
    rm *.aux *.fdb_latexmk *.fls *.log *.out *.synctex.gz *.toc *.back
