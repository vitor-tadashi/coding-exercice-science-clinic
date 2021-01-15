from pydantic import BaseModel


# Shared properties
class Procedure(BaseModel):
    hcpcs_code: str
    hcpcs_description: str
    state: str
    services: int
    average_medicare_allowed_amount: float
    min_average_medicare_allowed_amount: float
    max_average_medicare_allowed_amount: float
    average_medicare_payment_amount: float
    min_average_medicare_payment_amount: float
    max_average_medicare_payment_amount: float
    average_medicare_standardized_amount: float
    min_average_medicare_standardized_amount: float
    max_average_medicare_standardized_amount: float
    average_submitted_charge_amount: float
    min_average_submitted_charge_amount: float
    max_average_submitted_charge_amount: float
