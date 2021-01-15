from app.db.database import Database
from app.models.provider_type import ProviderType
from typing import List
import json


def get(db: Database, state: str, city: str) -> List[ProviderType]:
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
        response.append(ProviderType.parse_raw(json.dumps(row[1])))

    return response
