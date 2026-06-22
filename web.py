from fastapi import FastAPI, Request
from main import lambda_handler

app = FastAPI()

# Start with: uvicorn web:app --host 0.0.0.0 --port 8000
@app.post("/wompi/webhook")
async def wompi_webhook(request: Request):
    payload = await request.json()

    lambda_handler(payload, None)

    return {
        "status": "ok"
    }

@app.get("/")
async def health():
    return {"status": "running"}
