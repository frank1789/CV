FROM ubuntu:19.10
LABEL Francesco francesco.argentieri89@gmail.com
ENV DEBIAN_FRONTEND noninteractive

ENV DIR /cv

RUN apt-get -qy update && \
    apt-get upgrade -qy && \
    apt-get install -qy --no-install-recommends git \
    make \
    wget \
    curl \
    fonts-roboto \
    fonts-font-awesome \
    unzip \
    texlive-full \
    python-pygments gnuplot \
    texlive-base \
    texlive-latex-extra \
    texlive-xetex \
    texlive-fonts-extra \
    texlive-science \
    texlive-latex-recommended && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

RUN pip3 install dropbox

WORKDIR ${DIR}

COPY ./upload_file.py ${DIR}}

ENTRYPOINT ["/bin/bash", "-c", "make", "-f", "Makefile"]
