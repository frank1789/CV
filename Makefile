#!usr/bin/sh

CC    := xelatex
BB    := biber
FLAGS := -shell-escape -halt-on-error -interaction=batchmode
CV    := FrancescoArgentieri-Resume.tex
CL    := #modelling_eng-cover-letter.tex
BIB   := $(wildcard *.bib)

# color definition
blue   := \033[0;34m
yellow := \033[0;33m
green  := \033[0;32m
end    := \033[0m

.PHONY: clean resume
all: clean resume

build:
	docker build -t cv .

docker-run:
	docker run -it -v ${PWD}:/cv cv

resume:
	python3 resume.py


letter:
	@echo "${blue}----------------------------------${end}"
	@echo "${blue}===== Build xelatex document =====${end}"
	@echo "${blue}----------------------------------${end}"
	@echo
	@echo "${yellow}compling... x1${end}"
	${CC} ${FLAGS} ${CL}
	@echo "${yellow}compling... x2${end}"
	${CC} ${FLAGS} ${CL}
	@echo "${yellow}compling... x3${end}"
	${CC} ${FLAGS} ${CL}
	@echo "${green}Complete${end}"


clean:
	@echo "clean old build"
	rm -rf build
