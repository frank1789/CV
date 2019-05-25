FROM ubuntu:18.04

ENV DIR /CV
RUN apt-get -qy update && \
    apt-get upgrade -qy && \
    apt-get install -y --no-install-recommends git \
	make \
	wget \
	fonts-roboto \
    unzip \
    texlive-full \
    python-pygments gnuplot \
    texlive-base \
    texlive-latex-extra \
    texlive-xetex \
    texlive-fonts-extra \
    texlive-science \
    texlive-latex-recommended && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get clean

WORKDIR ${DIR}
ENTRYPOINT ["/bin/bash", "-c", "make", "-f", "Makefile"]
