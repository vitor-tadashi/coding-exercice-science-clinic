from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core import config

app = FastAPI(
    title="Healthcare providers utilization and Payment data",
    description="This solution was built from a test applied by Science and it was a great learning experience "
                "for me, since it was the first time I worked with FastAPI.",
    version="1.0.0",
    openapi_url="/healthcare/v1/openapi.json")

import uvicorn

app.include_router(api_router, prefix=config.API_V1)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")