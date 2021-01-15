from fastapi import APIRouter

from backend.app.api.v1.endpoints import procedures, provider_types

api_router = APIRouter()
api_router.include_router(procedures.router, tags=["procedures"])
api_router.include_router(provider_types.router, tags=["provider-types"])