![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![](https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white)
![](https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white)
![](https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white)
![](https://img.shields.io/badge/Pydantic-E92063.svg?style=for-the-badge&logo=Pydantic&logoColor=white)

## Installation:

```shell
git clone https://github.com/suntrackspb/bewise-api.git
```
```shell
cd bewise-api/
```
Edit .env file (if needed)
```dotenv
DB_NAME=postgres
DB_USER=postgres
DB_PASS=postgres
DB_HOST=db
DB_PORT=5432

PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin
```
```shell
docker-compose up --build
```
open api: http://localhost:8000/docs/

pgadmin: http://localhost:5050

Example Request:
```
curl -X 'POST' \
  'http://localhost:8000/api/v1/questions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 1
}'
```
