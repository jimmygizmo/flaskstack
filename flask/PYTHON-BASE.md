
### TODO: Using a new base image now - UPDATE ALL THIS INFO

## (old info) Python Base Image - Options, Details

NOTE: Although the image uses 3.10.10, the only good Pyenv versions which are currently available for local use via Venv which I might
consider are:   3.10.9  or  3.11.0. So we can't match exactly but all are close. And I'd prefer a close match with
a higher rather than lower Python version since Python is the base dependency. Hence, we stick with 3.11.1 in our
virtual environment, which is only to assist the IDE most of the time anyhow.
The local VE is mostly for helping the IDE do code inspection accurately while you type and for the occasional one-off
development task or experiment. The code we are really running and testing should usually be running in the container,
not in the VE you create with Pyenv. If you're not running your code with Docker-compose 98% of the time, you are
probably doing something shall we say, non-optimal. The whole point is to have a great running stack to develop against.

----

Large images are costly to move around and store and they slow down the code/test iteration cycle,
especially when development and/or deployment cycles are rapid. Nucleus is all about rapid
code/test cycles. (It is also all about self-contained, complete simulation of the deployed stack!)

I have had good luck with Bitnami images lately and they tend to be smaller and have many good features
and a good reputation. Base image details are outlined below.

I'm going with Bitnami for now because other popular alternatives are less secure, for one thing.

----

### Bitnami Python Image

    2023-02-11  -  bitnami/python  latest  c5757b37ea2c  645MB
    Version: 3.11.2
    Compressed size: 218MB
    Entrypoint: python

    Env:
    "PATH=/opt/bitnami/python/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "OS_ARCH=amd64",
    "OS_FLAVOUR=debian-11",
    "OS_NAME=linux",
    "APP_VERSION=3.11.2",
    "BITNAMI_APP_NAME=python"



