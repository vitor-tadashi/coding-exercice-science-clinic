FROM mdillon/postgis:9.6-alpine

ENV POSTGRES_DB cms
ENV POSTGRES_USER developer
ENV POSTGRES_PASSWORD development

COPY /data/* /data/
COPY ./create_schema.sql /docker-entrypoint-initdb.d/z_create_schema.sql