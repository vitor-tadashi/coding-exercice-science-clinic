from typing import List

from fastapi import APIRouter

from backend.app import crud
from backend.app.models.procedure import Procedure

router = APIRouter()


@router.get("/states/procedures/{hcpcs_code}/search", response_model=List[Procedure])
def get_state_procedures(
    hcpcs_code: str
):
    return crud.procedure.get_by_hcpcs_code(hcpcs_code)


@router.get("/procedures/search", response_model=List[Procedure])
def get_procedures(state: str, provider_type: str, offset: int = 0, limit: int = 50):
    return crud.procedure.get_by_state(state, provider_type, limit, offset)