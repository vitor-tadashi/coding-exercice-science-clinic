**0. Prerequisites:**

```
Pipenv https://pypi.org/project/pipenv/
```

**1. Installation:**
```shell script
pipenv install
```

**2. Run:**

```shell script
docker build ../../../infra/docker-postgis --tag postgis -f ../../../infra/docker-postgis/Dockerfile
docker run --rm -d -p 5432:5432 postgis 
uvicorn main:app --reload
```

Enjoy the API! http://127.0.0.1:8000/docs
