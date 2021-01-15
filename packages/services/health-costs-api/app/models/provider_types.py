from pydantic import BaseModel


# Shared properties
class ProviderTypes(BaseModel):
    provider_type: str
    services: int
    total_submitted_charge_amount: float
