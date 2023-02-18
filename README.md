# flaskstack

Backend REST API and database stack for standalone use or as a REST/data backend for The Nucleus Stack. PostgreSQL, Flask, FlaskRestful, SQLAlchemy, Alembic, Docker Compose. Includes example models and data that work with The Nucleus Stack bundled frontend app. Includes Miguel Grinberg's Microblog API, a best-practice REST app that uses the MIT license.

https://github.com/jimmygizmo/nucleus

### Included REST Service:

The best Python REST service you can build currently is one that follows the design patterns and philosophies of Miguel Grinberg, a leading author, open source software developer and teacher in the areas of Flask, Python, React, SQLAlchemy and many more important areas critical to building the very best, modern full stack applications.

I have included an adaptation of Miguel's Microblog API REST backend.

https://github.com/miguelgrinberg/microblog-api

The basic schema and set of features is very robust and ready to extend into production usage, based off of a solid foundation that includes:

- Full-featured, modern and robust authentication for web applications
- Full-featured User data and functionality for a web app
- Basic posting of text information with user-following, pagination and more

My exact roadmap for developing a robust yet generic REST application in FlaskStack is still taking shape, but there are two general goals:

- The Nucleus Stack frontend application will be extended to use what exists in the current REST API in FlaskStack as well as new features.
- The current REST API here will be extended to provide additional data sources and backend features to support new features in the Nucleus frontend as well as REST/SQL alternatives to data/features existing in Nucleus that are also provided by GraphQL, Apollo and MongoDB.

The goal is to provide a diversity of robust working code for adapting any kind of frontend feature to either a GraphQL backend or a REST/SQL backend, with matching robust backend code for all options.

Also note that the Apollo server in The Nucleus Stack is an API Federation service in addition to serving GraphQL. This means it can usinfy many kinds of backend data providers. Specifically, Apollo can seamlessly convert a REST API into a GraphQL API automatically. This is a capability easily leveraged when combinings The Nucleus Stack and FlaskStack, and you can always just connect your client direct to the REST service if that's what you want to do.

----

The Microblog API project is by Miguel Grinberg, Copyright 2021. It is released under the MIT license. The license file is included at /licenses/LICENSE-microblog-api

This project, FlaskStack, by Jim Mannix is also released under the MIT licenese and is Copyright 2023.  The license file for this project is included at /licenses/LICENSE.

