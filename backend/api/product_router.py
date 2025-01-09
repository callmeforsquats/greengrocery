from fastapi import APIRouter, Depends,HTTPException,UploadFile,File
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status
from ..core.database.db_helper import db_helper
from ..crud.products import *
from ..core.pymodels import *

router = APIRouter(prefix='/products',tags=["products"])

@router.post('/add',response_model=HTTPAnswer)
async def add_product(product_create:ProductCreate,session:AsyncSession=Depends(db_helper.get_session)):
    response = await create_product(product_create=product_create,session=session)
    return response

@router.get('/all-products',responses={status.HTTP_202_ACCEPTED:{'model':list[ProductRead]}})
async def get_products(session:AsyncSession=Depends(db_helper.get_session)):
    response=await get_all_products(session=session)
    return response


@router.get('/product/name/{name}',responses={status.HTTP_202_ACCEPTED:{'model':ProductRead},status.HTTP_400_BAD_REQUEST:{'model':HTTPAnswer}})
async def get_product_by_NAME(name:str,session:AsyncSession=Depends(db_helper.get_session)):
    response = await get_product_by_name(session=session,name=name)
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="no product with such name")


@router.get('/product/id/{id}',responses={status.HTTP_202_ACCEPTED:{'model':ProductRead},status.HTTP_400_BAD_REQUEST:{'model':HTTPAnswer}})
async def get_product_by_ID(id:int,session:AsyncSession=Depends(db_helper.get_session)):
    response = await get_product_by_id(session=session,id=id)
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="no product with such index")

@router.patch('/update/product/price/{name}',responses={status.HTTP_400_BAD_REQUEST:{'model':HTTPAnswer}})
async def update_product_PRICE(name:str,price:int,session:AsyncSession=Depends(db_helper.get_session)):
    response = await update_product_price(session=session,name=name,price=price)
    if response['detail']=="success":
        return response
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail={"no such product"})

@router.delete('/delete/product/{id}',responses={status.HTTP_200_OK:{'model':HTTPAnswer}})
async def delete_product(id:int,session:AsyncSession=Depends(db_helper.get_session)):
    response = await delete_product_by_id(session=session,id=id)
    return response

@router.patch('/update/product/picture/{name}',responses={status.HTTP_202_ACCEPTED:{'model':HTTPAnswer},status.HTTP_400_BAD_REQUEST:{'model':HTTPAnswer}})
async def update_product_PICTURE(name:str,picture:UploadFile=File(...),session:AsyncSession=Depends(db_helper.get_session)):
    response = await update_product_picture(session=session,name=name,picture=picture)
    if (response["detail"]!="no product"):
        return {'detail':'success'}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail={"no such product"})
