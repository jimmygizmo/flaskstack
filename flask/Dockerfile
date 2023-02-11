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

RUN mkdir /app/datavolume

# RUN chmod go+w /app/datavolume
# This chmod is aggressive and should give us 777. Trying to figure out the below issue.
# RESULT: This chmod did not help. Disabling it for removal. It was just an aggressive test.

# TODO: I did not see this touch work yet. Confirmed. Neither echo nor touch creates this file locally:
#   Not an issue. It's something simiple. This is not a trouble area. Leaving it for now
#   Also, I did try creating the dir at both /datavolume AND /app/datavolume thinking maybe app had different
#   perms (did not look at perms yet) but still nothing.
# Fixed an issue with the compose mount spec. Still nothing. Perms look good inside container too.
#   PARTIAL GOOD RESULT: Inside shell in cont, success MANUALLY executing this. Visible outside locally.
#   Exact manual successful command: "date > /app/datavolume/container-generated-test-file-in-exported-volume.txt"
#   Same command. Perms look good. This is rather interesting/unusual at this point. I'm sure it will be fixed soon.
#   /datavolume is not explicitly needed in this app yet, but I include the feature in all of my stacks.
#   I use /datavolume the same for all containers: General purpose cross-container data sharing and persistence.
RUN date > /app/datavolume/container-generated-test-file-in-exported-volume.txt


# For docker-compose execution, "flaskstack-postgres" must be up and acceptiing connections before
# "flaskstack-flask" starts.
# The wait-for-it.sh script will be run by docker-compose and will be passed
# arguments such that once it detects the "flaskstack-postgres" internal port is accepting connections, it will then
# bring up flask.
COPY ./wait-for-it.sh /app/wait-for-it.sh
RUN chmod o+x /app/wait-for-it.sh

