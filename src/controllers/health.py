from fastapi import APIRouter

health = APIRouter(prefix="/api")


@health.get("/health")
async def read_health():
    return {"message": "service is healthy"}
