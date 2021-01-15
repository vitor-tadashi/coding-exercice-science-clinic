from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core import config
from starlette.requests import Request
from app.db.database import Database
import uvicorn


app = FastAPI(
    title="Healthcare providers utilization and Payment data",
    description="This solution was built from a test applied by Science and it was a great learning experience "
                "for me, since it was the first time I worked with FastAPI.",
    version="1.0.0",
    openapi_url="/healthcare/v1/openapi.json")

app.include_router(api_router, prefix=config.API_V1)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Database()
    response = await call_next(request)
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
