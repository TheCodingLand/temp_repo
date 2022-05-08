
from fastapi import APIRouter

from fastapi.responses import HTMLResponse
from docs.get_rapidoc_html import get_rapidoc_html, get_rapidoc_oauth_receiver
from fastapi import Request
rapidoc_router = APIRouter()


@rapidoc_router.get('/rapidocs', include_in_schema=False)
async def get_rapidoc(request: Request) -> HTMLResponse:
    fast_api_app = request.app
    return get_rapidoc_html(
        openapi_url=fast_api_app.openapi_url,
        title=f'{fast_api_app.title} Docs'
    )
@rapidoc_router.get('/rapidocs/oauth-receiver', include_in_schema=False)
async def get_rapidoc() -> HTMLResponse:
    return get_rapidoc_oauth_receiver()

