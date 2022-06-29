# ITMEGASTAR test task

## how to run the project:
1. `make build` or `docker-compose build`
2. `make up` or `docker-compose up`
3. `make migrate` - apply migration files
4. `make fill_db` - fill DB with test data 
5. run tests: `make test`

> PS: if there are error: `django.db.utils.OperationalError: connection to server at "db" (172.23.0.2), port 5432 failed: Connection refused. Is the server running on that host and accepting TCP/IP connections?` shutdown the server and run again.

## Endpoints:
* `api/writers`