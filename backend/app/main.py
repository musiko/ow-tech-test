from fastapi import FastAPI

app = FastAPI(
    title="OW Copilot Usage API",
    summary="API for OW Copilot Usage",
    version="0.0.1",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
