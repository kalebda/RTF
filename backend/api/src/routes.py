from fastapi import APIRouter

from .core import schema

router = APIRouter()


@router.get("/service-info", response_model=schema.ServiceInfo, tags=["discovery"])
async def service_info():
    """
    Show information about this service.
    """
    return schema.service_info_response
