from typing import List

from fastapi import APIRouter, Depends

from app import crud
from app.models.procedure import Procedure
from app.models.provider_type import ProviderTypeEnum
from app.api.util.db import get_db
from app.db.database import Database

router = APIRouter()


@router.get("/states/procedures/{hcpcs_code}/search", response_model=List[Procedure])
def get_state_procedures(
        db: Database = Depends(get_db),
        hcpcs_code: str = '50590'
):
    return crud.procedure.get_by_hcpcs_code(db=db, hcpcs_code=hcpcs_code)


@router.get("/procedures/search", response_model=List[Procedure])
def get_procedures(
        db: Database = Depends(get_db),
        state: str = 'CA',
        provider_type: ProviderTypeEnum = ProviderTypeEnum.urology,
        offset: int = 0,
        limit: int = 50):
    return crud.procedure.get_by_state(db=db, state=state, provider_type=provider_type.value, limit=limit,
                                       offset=offset)


@router.get("/procedures/geo/search", response_model=List[Procedure])
def get_procedures_within_region(
        db: Database = Depends(get_db),
        west_limit: str = '-124.7',
        south_limit: str = '36.65',
        east_limit: str = '-120.16',
        north_limit: str = 38.95,
        offset: int = 0,
        limit: int = 50):
    return crud.procedure.get_inside_polygon(db=db, west_limit=west_limit, south_limit=south_limit,
                                             east_limit=east_limit, north_limit=north_limit,
                                             limit=limit, offset=offset)
