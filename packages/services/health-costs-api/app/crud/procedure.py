from app.db.database import Database
from app.models.procedure import Procedure
from typing import List
import json


def get_by_hcpcs_code(db: Database, hcpcs_code: str) -> List[Procedure]:
    sql_query = "".join(["select json_build_object('state', state, ",
                         "'hcpcs_code', hcpcs_code, ",
                         "'hcpcs_description', hcpcs_description, ",
                         "'services', sum(services), ",
                         "'medicare_beneficiaries', sum(medicare_beneficiaries), ",
                         "'average_medicare_allowed_amount', avg(average_medicare_allowed_amount), ",
                         "'min_average_medicare_allowed_amount', min(average_medicare_allowed_amount), ",
                         "'max_average_medicare_allowed_amount', max(average_medicare_allowed_amount), ",
                         "'average_medicare_payment_amount', avg(average_medicare_payment_amount), ",
                         "'min_average_medicare_payment_amount', min(average_medicare_payment_amount), ",
                         "'max_average_medicare_payment_amount', max(average_medicare_payment_amount), ",
                         "'average_medicare_standardized_amount', avg(average_medicare_standardized_amount), ",
                         "'min_average_medicare_standardized_amount', min(average_medicare_standardized_amount), ",
                         "'max_average_medicare_standardized_amount', max(average_medicare_standardized_amount), ",
                         "'average_submitted_charge_amount', avg(average_submitted_charge_amount), ",
                         "'min_average_submitted_charge_amount', min(average_submitted_charge_amount), ",
                         "'max_average_submitted_charge_amount', max(average_submitted_charge_amount)) ",
                         "from cms_medicare ",
                         "where hcpcs_code = %(hcpcs_code)s ",
                         "group by state, hcpcs_code, hcpcs_description ",
                         "order by state"])

    result = db.query(sql_query, {"hcpcs_code": hcpcs_code})
    response = []
    for row in result:
        response.append(Procedure.parse_raw(json.dumps(row[0])))

    return response


def get_by_state(db: Database, state: str, provider_type: str, limit: int, offset: int) -> List[Procedure]:
    sql_query = "".join(["select json_build_object('state', state, ",
                         "'hcpcs_code', hcpcs_code, ",
                         "'hcpcs_description', hcpcs_description, ",
                         "'services', sum(services), ",
                         "'medicare_beneficiaries', sum(medicare_beneficiaries), ",
                         "'average_medicare_allowed_amount', avg(average_medicare_allowed_amount), ",
                         "'min_average_medicare_allowed_amount', min(average_medicare_allowed_amount), ",
                         "'max_average_medicare_allowed_amount', max(average_medicare_allowed_amount), ",
                         "'average_medicare_payment_amount', avg(average_medicare_payment_amount), ",
                         "'min_average_medicare_payment_amount', min(average_medicare_payment_amount), ",
                         "'max_average_medicare_payment_amount', max(average_medicare_payment_amount), ",
                         "'average_medicare_standardized_amount', avg(average_medicare_standardized_amount), ",
                         "'min_average_medicare_standardized_amount', min(average_medicare_standardized_amount), ",
                         "'max_average_medicare_standardized_amount', max(average_medicare_standardized_amount), ",
                         "'average_submitted_charge_amount', avg(average_submitted_charge_amount), ",
                         "'min_average_submitted_charge_amount', min(average_submitted_charge_amount), ",
                         "'max_average_submitted_charge_amount', max(average_submitted_charge_amount)) ",
                         "from cms_medicare ",
                         "where state = %(state)s and provider_type = %(provider_type)s ",
                         "group by state, hcpcs_code, hcpcs_description ",
                         "LIMIT %(limit)s OFFSET %(offset)s"])

    result = db.query(sql_query, {'state': state, 'provider_type': provider_type, 'limit': limit, 'offset': offset})
    response = []
    for row in result:
        print(Procedure.parse_raw(json.dumps(row[0])))
        response.append(Procedure.parse_raw(json.dumps(row[0])))

    return response


def get_inside_polygon(db: Database, west_limit: str, south_limit: str, east_limit: str, north_limit: str, limit: int, offset: int) \
        -> List[Procedure]:
    sql_query = "".join(["select json_build_object('state', state, ",
                         "'hcpcs_code', hcpcs_code, ",
                         "'hcpcs_description', hcpcs_description, ",
                         "'services', sum(services), ",
                         "'medicare_beneficiaries', sum(medicare_beneficiaries), ",
                         "'average_medicare_allowed_amount', avg(average_medicare_allowed_amount), ",
                         "'min_average_medicare_allowed_amount', min(average_medicare_allowed_amount), ",
                         "'max_average_medicare_allowed_amount', max(average_medicare_allowed_amount), ",
                         "'average_medicare_payment_amount', avg(average_medicare_payment_amount), ",
                         "'min_average_medicare_payment_amount', min(average_medicare_payment_amount), ",
                         "'max_average_medicare_payment_amount', max(average_medicare_payment_amount), ",
                         "'average_medicare_standardized_amount', avg(average_medicare_standardized_amount), ",
                         "'min_average_medicare_standardized_amount', min(average_medicare_standardized_amount), ",
                         "'max_average_medicare_standardized_amount', max(average_medicare_standardized_amount), ",
                         "'average_submitted_charge_amount', avg(average_submitted_charge_amount), ",
                         "'min_average_submitted_charge_amount', min(average_submitted_charge_amount), ",
                         "'max_average_submitted_charge_amount', max(average_submitted_charge_amount)) ",
                         "from cms_medicare ",
                         "where ST_CONTAINS(ST_MakeEnvelope(%(west_limit)s, %(south_limit)s, %(east_limit)s, "
                         "%(north_limit)s, 4326), ST_SetSRID(geom, 4326))",
                         "group by state, hcpcs_code, hcpcs_description ",
                         "LIMIT %(limit)s OFFSET %(offset)s"])

    result = db.query(sql_query,
                      {'west_limit': west_limit, 'south_limit': south_limit, 'east_limit': east_limit,
                       'north_limit': north_limit, 'limit': limit, 'offset': offset})
    response = []
    for row in result:
        print(Procedure.parse_raw(json.dumps(row[0])))
        response.append(Procedure.parse_raw(json.dumps(row[0])))

    return response
