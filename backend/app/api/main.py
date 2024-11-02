from fastapi import APIRouter

from app.api.routes import usage

api_router = APIRouter()
api_router.include_router(usage.router, prefix="/usage", tags=["usage"])
