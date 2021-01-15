# Backend Challenge - Science

## Install and Run
The solution uses [python](https://www.python.org/g) and [docker](https://docs.docker.com/docker-for-mac/install/). Please go check them out if you don't have them locally installed.

```shell script
git clone https://github.com/vitor-tadashi/coding-exercice-science-clinic.git
```

After cloning the solution you will need to download the data from CMS:
1. First go to this webpage https://data.cms.gov/Medicare-Physician-Supplier/Medicare-Provider-Utilization-and-Payment-Data-Phy/fs4p-t5eq/data
2. Click on "Export"
![export-button](img/export-cms.png)
3. Click on "Download" > "CSV"
4. Save as "medicare_data.csv" inside the folder "./infra/docker-postgis/data"

Unfortunately it's a 2-gigabyte file and I can't upload in the repo, the data from this file will be ingested in the PostgreSQL database.

After that please execute:

```shell script
cd ./coding-exercice-science-clinic
docker-compose build
docker-compose up
```

If you want to run in background mode:
```shell script
docker-compose up -d
```

The solution has a low start because it needs to ingest the data, but it doesn't take too long.

## Schema

All API access is over http, and the data is sent and received as JSON.

```bash
curl -X GET "http://localhost:8080/healthcare/v1/states/procedures/50590/search" -H  "accept: application/json""

HTTP/1.1 200 OK
content-length: 686 
content-type: application/json 
date: Fri,15 Jan 2021 10:57:32 GMT 
server: uvicorn 

[
  {
    "hcpcs_code": "50590",
    "hcpcs_description": "Shock wave crushing of kidney stones",
    "state": "AK",
    "services": 52,
    "average_medicare_allowed_amount": 660.20265625,
    "min_average_medicare_allowed_amount": 569.0853125,
    "max_average_medicare_allowed_amount": 751.32,
    "average_medicare_payment_amount": 501.42459375,
    "min_average_medicare_payment_amount": 428.3096875,
    "max_average_medicare_payment_amount": 574.5395,
    "average_medicare_standardized_amount": 460.705125,
    "min_average_medicare_standardized_amount": 453.054,
    "max_average_medicare_standardized_amount": 468.35625,
    "average_submitted_charge_amount": 1320.2085,
    "min_average_submitted_charge_amount": 1191.417,
    "max_average_submitted_charge_amount": 1449
  },
  ...
]
```

## API Documentation

Great! Now you're ready to go to `http://localhost:8080/docs/` and try out the example!