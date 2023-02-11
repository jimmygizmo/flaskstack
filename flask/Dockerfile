FROM bitnami/python:3.11.1
# 2023-02-11  -  bitnami/python  latest  c5757b37ea2c  644MB
# Version: 3.11.1
# Base OS flavor: debian-11
# Compressed size: 218MB
# Entrypoint: "python -V"  # NOTE: Just a test/placeholder for now.

# TODO: The above entry point did not work. (not in path?) But I can see this is the path to python:
# /opt/bitnami/python/bin/python

# TODO: Entry point will become the startup command for flask or possibly supervisord to manage flask start/restart.

# TODO: This image size seems large. It should be possible to shrink it substantially.
#  Plan is to remove uneeded-content from the image and assess before considering other base images.
#  I want to avoid using an Alpine base image for security and other reasons.

# NOTE: The /app directory already exists in this base image.

RUN mkdir /datavolume

RUN touch /datavolume/container-generated-test-file-in-exported-volume.txt


# For docker-compose execution, "flaskstack-postgres" must be up and acceptiing connections before
# "flaskstack-flask" starts.
# The wait-for-it.sh script will be run by docker-compose and will be passed
# arguments such that once it detects the "flaskstack-postgres" internal port is accepting connections, it will then
# bring up flask.
COPY ./wait-for-it.sh /app/wait-for-it.sh
RUN chmod o+x /app/wait-for-it.sh

