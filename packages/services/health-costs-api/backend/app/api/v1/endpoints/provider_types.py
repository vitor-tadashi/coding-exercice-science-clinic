from typing import List, Optional

from fastapi import APIRouter

from backend.app import crud
from backend.app.models.provider_types import ProviderTypes

router = APIRouter()


@router.get("/provider-types/search", response_model=List[ProviderTypes])
def get_provider_types(
    state: str,
    city: Optional[str] = None
):
    return crud.provider_types.get(state, city)
