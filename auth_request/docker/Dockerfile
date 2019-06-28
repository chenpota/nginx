FROM ubuntu:16.04

RUN apt-get update \
 && apt-get install -y --force-yes --no-install-recommends \
        build-essential \
        nginx \
        python3-dev \
        python3-pip \
        python3-venv \
        python3-wheel \
        supervisor \
 && pip3 install pip --upgrade \
 && python3 -m venv /venv \
 && /venv/bin/pip3 install pip --upgrade \
 && /venv/bin/pip3 install wheel \
 && /venv/bin/pip3 install \
        Flask
