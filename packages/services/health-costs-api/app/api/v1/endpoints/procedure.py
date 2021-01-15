from typing import List

from fastapi import APIRouter

from app import crud
from app.models.procedure import Procedure
from app.models.provider_type import ProviderTypeEnum

router = APIRouter()


@router.get("/states/procedures/{hcpcs_code}/search", response_model=List[Procedure])
def get_state_procedures(
    hcpcs_code: str
):
    return crud.procedure.get_by_hcpcs_code(hcpcs_code)


@router.get("/procedures/search", response_model=List[Procedure])
def get_procedures(state: str, provider_type: ProviderTypeEnum, offset: int = 0, limit: int = 50):
    return crud.procedure.get_by_state(state=state, provider_type=provider_type.value, limit=limit, offset=offset)


@router.get("/procedures/geo/search", response_model=List[Procedure])
def get_procedures_within_region(west_limit: str = '-124.7', south_limit: str = '36.65', east_limit: str = '-120.16',
                                 north_limit: str = 38.95, offset: int = 0, limit: int = 50):
    return crud.procedure.get_inside_polygon(west_limit=west_limit, south_limit=south_limit, east_limit=east_limit,
                                             north_limit=north_limit, limit=limit, offset=offset)