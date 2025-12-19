from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Counter API")

# Configure CORS - in production, replace "*" with your specific domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production: ["https://yourdomain.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory counter (resets on server restart)
counter = {"count": 0}


class CounterResponse(BaseModel):
    count: int


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy", "service": "counter-api"}


@app.post("/increment", response_model=CounterResponse)
async def increment_counter():
    """Increment the counter and return the new value"""
    counter["count"] += 1
    return {"count": counter["count"]}


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Counter API",
        "endpoints": {
            "health": "GET /health",
            "increment": "POST /increment",
        }
    }
