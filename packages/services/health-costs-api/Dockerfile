FROM python:3.7

RUN pip install fastapi uvicorn typing pydantic psycopg2 base

EXPOSE 8080
ENV POSTGRES_SERVER postgis
ENV POSTGRES_USER developer
ENV POSTGRES_PASSWORD development
ENV POSTGRES_DB cms

COPY ./ /

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]