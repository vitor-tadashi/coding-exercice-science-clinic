import csv
import requests
import psycopg2

api_key = ""
api_url = "https://maps.googleapis.com/maps/api/geocode/json"


def ingest_cms_medicare_data():
    addresses = set()
    geolocation = dict()
    data = list()

    with open('medicare_SF_CA.csv', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader, None)
        for row in reader:
            json_data = {
                "national_provider_identifier": row[0],
                "provider_last_organization_name": row[1],
                "provider_first_name": row[2],
                "provider_middle_name": row[3],
                "provider_credentials": row[4],
                "provider_gender": row[5],
                "entity_type": row[6],
                "address": row[7],
                "city": row[9],
                "zip_code": row[10],
                "state": row[11],
                "country_code": row[12],
                "geom": "",
                "provider_type": row[13],
                "medicare_participation_indicator": row[14],
                "service_place": row[15],
                "hcpcs_code": row[16],
                "hcpcs_description": row[17],
                "hcpcs_drug": row[18],
                "services": row[19],
                "medicare_beneficiaries": row[20],
                "distinct_medicare_beneficiaries": row[21],
                "average_medicare_allowed_amount": row[22],
                "average_submitted_charge_amount": row[23],
                "average_medicare_payment_amount": row[24],
                "average_medicare_standardized_amount": row[25]
            }
            data.append(json_data)
            addresses.add(", ".join([row[7], row[9], row[11], row[12]]))
    print(len(addresses))
    with open('latitude_longitude.csv', 'w') as f:
        for address in addresses:
            response = requests.get('{0}?address="{1}"&key={2}'.format(api_url, address, api_key))
            response_json = response.json()
            if len(response_json["results"]) > 0:
                print(response_json["results"][0]["geometry"]["location"])
                geolocation[address] = response_json["results"][0]["geometry"]["location"]
                f.write("%s,%s\n" % (address, response_json["results"][0]["geometry"]["location"]))

    save(data, geolocation)


def save(data, geolocation):
    conn = psycopg2.connect(host="localhost", port=5432, database="cms", user="developer", password="development")
    cur = conn.cursor()

    sql = "INSERT INTO cms_medicare(national_provider_identifier, provider_last_organization_name, " \
          "provider_first_name, provider_middle_name, provider_credentials, provider_gender," \
          "entity_type, address, city, zip_code, state, country_code, geom, provider_type," \
          "medicare_participation_indicator, service_place, hcpcs_code, hcpcs_description," \
          "hcpcs_drug, services, medicare_beneficiaries, distinct_medicare_beneficiaries," \
          "average_medicare_allowed_amount, average_submitted_charge_amount," \
          "average_medicare_payment_amount, average_medicare_standardized_amount) " \
          "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
          " %s, ST_POINT(%s, %s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    for item in data:
        address = ", ".join([item["address"], item["city"], item["state"], item["country_code"]])
        try:
            latitude = geolocation[address]['lat']
            longitude = geolocation[address]['lng']

            print(item)
            cur.execute(sql, (item["national_provider_identifier"], item["provider_last_organization_name"],
                              item["provider_first_name"], item["provider_middle_name"],
                              item["provider_credentials"], item["provider_gender"],
                              item["entity_type"], item["address"],
                              item["city"], item["zip_code"],
                              item["state"], item["country_code"],
                              longitude, latitude, item["provider_type"],
                              item["medicare_participation_indicator"], item["service_place"],
                              item["hcpcs_code"], item["hcpcs_description"],
                              item["hcpcs_drug"], item["services"],
                              item["medicare_beneficiaries"], item["distinct_medicare_beneficiaries"],
                              item["average_medicare_allowed_amount"], item["average_submitted_charge_amount"],
                              item["average_medicare_payment_amount"], item["average_medicare_standardized_amount"]))
        except:
            print("An exception occurred")

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    ingest_cms_medicare_data()