# ITMEGASTAR test task

## how to run the project:
1. `make build` or `docker-compose build`
2. `make up` or `docker-compose up`
   1. way #1
      1. `make migrate` - apply migration files
      2. `make fill_db` - fill DB with test data
   2. way#2 *(recommended)*
      1. `make init` (migration + filling)
3. run tests: `make test`

> PS: if there are error: `django.db.utils.OperationalError: connection to server at "db" (172.23.0.2), port 5432 failed: Connection refused. Is the server running on that host and accepting TCP/IP connections?` shutdown the server and run again.

## Endpoints:
* `api/writers`