FROM python:3.10-slim
# 2023-02-18  -  ______________  latest  a101c542dbeb  126MB
# Version (Python): 3.10.10
# Base OS flavor: Debian GNU/Linux 11 (bullseye)
# Compressed size: 46MB
# Entrypoint: (none)
# Path to Python: /usr/local/bin/python
# Path to bash: /bin/bash
#   NOTE: A bash entry-point is common with Flask services and the FlaskStack API currently uses one.
#   TODO: Entrypoint could become the startup command for supervisord to manage app start/restart.

ENV FLASK_APP flaskstack.py
#ENV FLASK_ENV production
ENV FLASK_ENV development
ENV FLASK_DEBUG 1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./api /app/api/
COPY ./migrations /app/migrations/
COPY flaskstack.py config.py boot.sh /app/

COPY ./wait-for-it.sh /app/
RUN chmod o+x /app/wait-for-it.sh

EXPOSE 5000


#CMD ./boot.sh


# ------------------------------------------------------------------------------------------------------------------
# EVERYTHING BELOW HERE WAS THE ORIGINAL DOCKERFILE - prior to fitting it to Microblog API
# Scroll down to the very end for detail captured about the NEW image (python:3.10-slim)
# ------------------------------------------------------------------------------------------------------------------
# Below here all went with: #FROM bitnami/python:3.11.1
# The purpose was different and the base image is different, so we may need almost nothing from here:
# ITEMS DISABLED IMMEDIATELY AFTER CHANGEOVER MARKED WITH ####--####

####--####WORKDIR /app

####--####RUN pip install --upgrade pip

####--####RUN pip install --upgrade setuptools

# RUN pip install --upgrade wheel  # Needed?


# For docker-compose execution, "flaskstack-postgres" must be up and acceptiing connections before
# "flaskstack-flask" starts.
# The wait-for-it.sh script will be run by docker-compose and will be passed
# arguments such that once it detects the "flaskstack-postgres" internal port is accepting connections, it will then
# bring up flask.
####--####COPY ./wait-for-it.sh /app/wait-for-it.sh
####--####RUN chmod o+x /app/wait-for-it.sh


# NOTE: The /app directory already exists in this base image.
# Create the datavolume directory which is exported and mounted externally/locally on the local host machine.
####--####RUN mkdir /app/datavolume

####--####COPY requirements.txt .

####--####RUN pip install -r requirements.txt

# Disabled for the moment.
#COPY nucleus.py .

# COPY - IMPORTANT NUANCE: trailing slash on source dir will copy only the contents. (COPY ./nucleus .)
#   Remove trailing slash and TODO: Observe and update. We'll re-enable this shortly.
#COPY ./nucleus .

####--####EXPOSE 5000


# ------------------------------------------------------------------------------------------------------------------
# DETAILS ON NEW IMAGE BELOW HERE:
# ------------------------------------------------------------------------------------------------------------------

# #################### NEW BASE IMAGE DETAILS
# ENV:
# PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# LANG=C.UTF-8
# GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D
# PYTHON_VERSION=3.10.10
# PYTHON_PIP_VERSION=22.3.1
# PYTHON_SETUPTOOLS_VERSION=65.5.1
# PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/1a96dc5acd0303c4700e02655aefd3bc68c78958/public/get-pip.py
# PYTHON_GET_PIP_SHA256=d1d09b0f9e745610657a528689ba3ea44a73bd19c60f4c954271b790c71c2653
# "Cmd": [
#     "/bin/sh",
#     "-c",
#     "#(nop) ",
#     "CMD [\"python3\"]"
# ],

#root@eb2f68b7e67b:/# uname -a
#Linux eb2f68b7e67b 5.15.49-linuxkit #1 SMP Tue Sep 13 07:51:46 UTC 2022 x86_64 GNU/Linux

#root@eb2f68b7e67b:/# which python
#/usr/local/bin/python

#root@eb2f68b7e67b:/# which python3
#/usr/local/bin/python3

#root@eb2f68b7e67b:/# python -V
#Python 3.10.10

#root@eb2f68b7e67b:/# python3 -V
#Python 3.10.10

#root@eb2f68b7e67b:/# cat /etc/os-release
#PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
#NAME="Debian GNU/Linux"
#VERSION_ID="11"
#VERSION="11 (bullseye)"
#VERSION_CODENAME=bullseye
#ID=debian
#HOME_URL="https://www.debian.org/"
#SUPPORT_URL="https://www.debian.org/support"
#BUG_REPORT_URL="https://bugs.debian.org/"


