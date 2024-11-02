from fastapi import FastAPI

from app.api.main import api_router

app = FastAPI(
    title="OW Copilot Usage API",
    summary="API for OW Copilot Usage",
    version="0.0.1",
)


app.include_router(api_router)
