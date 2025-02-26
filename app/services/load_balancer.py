import random

import aiohttp
from loguru import logger
from starlette import status

from app.settings.settings import api_settings, EnvMode
from app.utils.cloud_headers import get_cloud_run_auth_header
from app.utils.decorators import retry_request


class LoadBalancer:
    last_chosen_service = None

    @staticmethod
    def get_random_service(urls):
        available_services = [
            url for url in urls if url != LoadBalancer.last_chosen_service
        ]

        chosen_service = random.choice(available_services)

        LoadBalancer.last_chosen_service = chosen_service

        return chosen_service

    @staticmethod
    @retry_request
    async def make_request_to_service(url: str, body: dict) -> dict:
        logger.info(f"Making request to service: {url} with body: {body}")
        async with aiohttp.ClientSession() as session:
            headers = {
                "Content-Type": "application/json",
                "X-API-Key": api_settings.API_KEY,
            }
            if api_settings.ENV != EnvMode.DEV:
                headers.update(get_cloud_run_auth_header(url))
            async with session.post(url, headers=headers, json=body) as response:
                if response.status == status.HTTP_200_OK:
                    return await response.json()
                else:
                    raise Exception(f"Error: {response.status}")
