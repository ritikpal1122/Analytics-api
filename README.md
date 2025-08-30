# Analytics API using fast api with time series postgres
==============================================
### Overview
This is a simple API using FastAPI to interact with a PostgreSQL database for time series data.
### Requirements
- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- psycopg2
- pandas
### Installation


## Docker 
- ` docker build -t analytics-api -f  Dockerfile.web .`
- `docker run analytics-api`

-  `docker-compose up --watch`
-  ` docker-compose down ` or `docker -compose down -v` (to remove volumes ) 
