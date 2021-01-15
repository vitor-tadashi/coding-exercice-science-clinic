from fastapi import APIRouter

from app.api.v1.endpoints import provider_type, procedure

api_router = APIRouter()
api_router.include_router(procedure.router, tags=["procedures"])
api_router.include_router(provider_type.router, tags=["provider-types"])