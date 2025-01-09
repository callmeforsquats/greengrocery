from fastapi import APIRouter
from .product_router import router as product_router

router = APIRouter(prefix="/api",tags=['API'])
router.include_router(product_router)


@router.get('/')
def hello():
    return {"msg","hello"}