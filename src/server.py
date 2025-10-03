import uvicorn
from config import config
from controllers.health import health
from controllers.example import example
from fastapi import FastAPI

app = FastAPI()

# Register your routes and routers
app.include_router(health)
app.include_router(example)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(config["PORT"]))
