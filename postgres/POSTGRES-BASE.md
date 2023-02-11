
## Postgres Base Image - Options, Details

TODO: Convert this file to .md format. It is raw text currently.

----

Large images are costly to move around and store and they slow down the code/test iteration cycle,
especially when development and/or deployment cycles are rapid. Nucleus is all about rapid
code/test cycles. (It is also all about self-contained, complete simulation of the deployed stack!)

I have had good luck with Bitnami images lately and they tend to be smaller and have many good features
and a good reputation. Both the standard PostgreSQL image and the Bitnami version are outlined below.

I'm going with Bitnami for now.


BITNAMI POSTGRES IMAGE
----------------------

FROM bitnami/postgresql:latest
# 2023-02-10  -  bitnami/postgresql  latest  f576e9b9b432  275MB
# Compressed size: 88MB

Path to map dbvolume to: /bitnami/postgresql


"PATH=/opt/bitnami/common/bin:/opt/bitnami/postgresql/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
"HOME=/",
"OS_ARCH=amd64",
"OS_FLAVOUR=debian-11",
"OS_NAME=linux",
"APP_VERSION=15.2.0",
"BITNAMI_APP_NAME=postgresql",
"LANG=en_US.UTF-8",
"LANGUAGE=en_US:en",
"NSS_WRAPPER_LIB=/opt/bitnami/common/lib/libnss_wrapper.so"

ENTRYPOINT: "/opt/bitnami/scripts/postgresql/run.sh"

----------------------------------------------------------------------------------------------------------------------

OFFICIAL POSTGRES IMAGE - VERSION: 15.2.1
-------------------------------------------

2023-02-11  -  postgres  latest  680aba37fd0f  379MB
# Compressed size: 134MB

Path to map dbvolume to: /var/lib/postgresql/data

"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/15/bin",
"GOSU_VERSION=1.16",
"LANG=en_US.utf8",
"PG_MAJOR=15",
"PG_VERSION=15.2-1.pgdg110+1",
"PGDATA=/var/lib/postgresql/data"

----------------------------------------------------------------------------------------------------------------------

