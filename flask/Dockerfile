FROM bitnami/python:3.11.1
# 2023-02-11  -  bitnami/python  latest  c5757b37ea2c  644MB
# Version: 3.11.1
# Base OS flavor: debian-11
# Compressed size: 218MB
# Entrypoint: By default, the image just exits after starting.
# Path to Python: /opt/bitnami/python/bin/python

# TODO: Entry point will become the startup command for flask or possibly supervisord to manage flask start/restart.

# TODO: This image size seems large. It should be possible to shrink it substantially.
#  Plan is to remove uneeded-content from the image and assess before considering other base images.
#  I want to avoid using an Alpine base image for security and other reasons.

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools

# RUN pip install --upgrade wheel  # Needed?


# For docker-compose execution, "flaskstack-postgres" must be up and acceptiing connections before
# "flaskstack-flask" starts.
# The wait-for-it.sh script will be run by docker-compose and will be passed
# arguments such that once it detects the "flaskstack-postgres" internal port is accepting connections, it will then
# bring up flask.
COPY ./wait-for-it.sh /app/wait-for-it.sh
RUN chmod o+x /app/wait-for-it.sh


# NOTE: The /app directory already exists in this base image.
# Create the datavolume directory which is exported and mounted externally/locally on the local host machine.
RUN mkdir /app/datavolume

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY nucleus.py .

EXPOSE 5000

