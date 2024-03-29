FROM ubuntu:latest
LABEL version="0.1.0" maintaner="Francesco Argentieri <francesco.argentieri89@gmail.com>"
ENV DEBIAN_FRONTEND noninteractive

ENV DIR /cv

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -qy --no-install-recommends git \
    make \
    wget \
    curl \
    fonts-roboto \
    fonts-font-awesome \
    unzip \
    gnuplot \
    texlive-full \
    texlive-base \
    texlive-latex-extra \
    texlive-xetex \
    texlive-fonts-extra \
    texlive-science \
    texlive-latex-recommended \
    python3-pip python3-dev \
    python3-pygments \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python 
    # && pip3 install --upgrade pip

RUN pip3 install --user jinja2 dropbox

WORKDIR ${DIR}

ENTRYPOINT ["/bin/bash", "-c", "make", "-f", "Makefile"]
