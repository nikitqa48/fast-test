from fastapi import APIRouter
from src.endpoints.testing import test


router = APIRouter()
router.include_router(test, tags=('test',))
