FROM ubuntu:18.04

ENV DIR /CV
RUN apt-get -qq update && \
	rm -rf /var/lib/apt/lists/* \
	apt-get install -y --no-install-recommends git \
	make \
	wget \
	fonts-robot \
	apt-transport-https \
    unzip && \
    apt-get install -y texlive-base \
        texlive-latex-extra \
        texlive-xetex \
        texlive-lang-cyrillic \
        texlive-fonts-extra \
        texlive-science \
        texlive-latex-recommended \
        latexmk

WORKDIR ${DIR}
ENTRYPOINT ["/bin/bash", "-c", "make", "-f", "Makefile"]
