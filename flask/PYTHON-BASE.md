
## Python Base Image - Options, Details

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



