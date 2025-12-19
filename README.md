# Counter API Backend

FastAPI backend for the Counter mobile app.

## Quick Start

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Server will be available at `http://localhost:8000`

## API Endpoints

### GET /
Returns API information and available endpoints.

**Response:**
```json
{
  "message": "Counter API",
  "endpoints": {
    "health": "GET /health",
    "increment": "POST /increment"
  }
}
```

### GET /health
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy",
  "service": "counter-api"
}
```

### POST /increment
Increments the counter and returns the new value.

**Response:**
```json
{
  "count": 1
}
```

## Testing

```bash
# Health check
curl http://localhost:8000/health

# Increment counter
curl -X POST http://localhost:8000/increment

# Increment again
curl -X POST http://localhost:8000/increment
```

## Deployment

See `../docs/BACKEND_SETUP.md` for detailed deployment instructions.

### Quick Deploy to Railway

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway init
railway up
```

### Quick Deploy to Render

1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Create new Web Service
4. Connect your repository
5. Render will auto-detect and deploy

## Environment Variables

- `PORT`: Port to run the server on (default: 8000)
- `ENVIRONMENT`: Environment name (development/production)

## CORS Configuration

Currently configured to allow all origins (`*`) for development.

For production, update `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specify your domain
    ...
)
```

## Notes

- Counter is stored in memory and resets on server restart
- For production, use a database (PostgreSQL, MongoDB, etc.)
- See `../docs/PRODUCTION.md` for scaling considerations
