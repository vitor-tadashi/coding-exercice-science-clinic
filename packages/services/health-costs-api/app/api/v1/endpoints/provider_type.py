from typing import List, Optional

from fastapi import APIRouter

from app import crud
from app.models.provider_type import ProviderType

router = APIRouter()


@router.get("/provider-types/search", response_model=List[ProviderType])
def get_provider_types(
    state: str,
    city: Optional[str] = None
):
    return crud.provider_types.get(state, city)
