from fastapi import FastAPI

from backend.app.api.v1.api import api_router
from backend.app.core import config
app = FastAPI()

import uvicorn

app.include_router(api_router, prefix=config.API_V1)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")