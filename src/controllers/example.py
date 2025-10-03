from fastapi import APIRouter

example = APIRouter(prefix="/api/v1")


@example.get("/example")
async def read_example():
    return {"message": "hello"}
