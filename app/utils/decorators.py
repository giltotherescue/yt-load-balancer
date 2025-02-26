import asyncio
from functools import wraps

from fastapi import HTTPException
from loguru import logger
from starlette import status

from app.settings.constants import MAX_RETRIES


def retry_request(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        retries = kwargs.get("retries", 0)
        while retries < MAX_RETRIES:
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                retries += 1
                logger.error(
                    f"Error in request. Attempt {retries}/{MAX_RETRIES}. Error: {str(e)}"
                )
                await asyncio.sleep(1)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Max retries exceeded.",
        )

    return wrapper
