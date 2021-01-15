from backend.app.db.database import Database
from backend.app.models.provider_types import ProviderTypes
from typing import List
import json


def get(state: str, city: str) -> List[ProviderTypes]:
    db = Database()

    sql_query = "".join(["select cast(sum(services * average_submitted_charge_amount) as bigint) as "
                         "total_submitted_charge_amount, ",
                         "json_build_object('provider_type', provider_type, ",
                         "'services', cast(sum(services) as integer), ",
                         "'total_submitted_charge_amount', cast(sum(services * average_submitted_charge_amount) as "
                         "bigint)) ",
                         "from cms_medicare ",
                         "where state = %(state)s AND (city = %(city)s OR %(city)s IS NULL) ",
                         "group by provider_type ",
                         "order by total_submitted_charge_amount desc"])

    result = db.query(sql_query, {"state": state, "city": city})
    response = []
    for row in result:
        response.append(ProviderTypes.parse_raw(json.dumps(row[1])))

    return response