from fastapi import HTTPException
from starlette.requests import Request

from app.settings.settings import api_settings


def require_api_key(request: Request):
    api_key = request.headers.get("X-API-Key")
    if api_key and api_key == api_settings.API_KEY:
        return True
    else:
        raise HTTPException(status_code=401, detail="Invalid API key")
