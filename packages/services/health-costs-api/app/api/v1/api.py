from fastapi import APIRouter

from app.api.v1.endpoints import provider_types, procedures

api_router = APIRouter()
api_router.include_router(procedures.router, tags=["procedures"])
api_router.include_router(provider_types.router, tags=["provider-types"])