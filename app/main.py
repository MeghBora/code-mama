from fastapi import FastAPI
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger("uvicorn.error")
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("API_PORT", 8000))  # Fallback to 8000 if not set
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
    logger.info(f"Server running on port {port}")
    