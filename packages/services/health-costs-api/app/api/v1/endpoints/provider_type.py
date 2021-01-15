from typing import List, Optional

from fastapi import APIRouter, Depends

from app import crud
from app.models.provider_type import ProviderType
from app.api.util.db import get_db
from app.db.database import Database

router = APIRouter()


@router.get("/provider-types/search", response_model=List[ProviderType])
def get_provider_types(
    db: Database = Depends(get_db),
    state: str = 'CA',
    city: Optional[str] = None
):
    return crud.provider_type.get(db=db, state=state, city=city)
