from contextlib import asynccontextmanager

from fastapi import FastAPI, Query, Depends

from app.services.auth import require_api_key
from app.services.load_balancer import LoadBalancer
from app.utils.get_services import get_all_cloud_run_service_uris

ALL_SERVICE_URLS = []


def init_services():
    global ALL_SERVICE_URLS
    ALL_SERVICE_URLS = get_all_cloud_run_service_uris()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_services()
    yield
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)


@app.get("/scrape")
async def load_balancer(
    channel_handle: str = Query(
        description="Channel handle to scrape", alias="channelHandle"
    ),
    max_videos: int = Query(
        10, description="Maximum number of videos to scrape", alias="maxVideos"
    ),
    service: LoadBalancer = Depends(LoadBalancer),
    _: bool = Depends(require_api_key),
):
    body = {"channel_handle": channel_handle, "max_videos": max_videos}
    service_url = f"{service.get_random_service(ALL_SERVICE_URLS)}/scrape"
    return await service.make_request_to_service(service_url, body)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
