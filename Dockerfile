FROM python:3.8.0a4-alpine3.9

RUN apk update
RUN apk upgrade
RUN apk add --no-cache --update \
    curl \
    bash \
    ncurses \
    make

RUN rm /var/cache/apk/*

RUN mkdir -p /app

WORKDIR /app

# COPY . ./

# Docker Whale prompt (which needs ncurses package for tput to work)
RUN printf 'export PS1="\[$(tput setaf 4)\] __v_\\n\[$(tput setaf 4)\]($(tput smul)₀   $(tput rmul)\/{\[$(tput sgr0)\] \\t \[$(tput setaf 5)\][\w]\[$(tput sgr0)\]\$ "' >> ~/.bashrc
