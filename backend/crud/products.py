from typing import Sequence
from fastapi import File, UploadFile
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from ..core.pymodels import *
from ..core.database.sqlmodels import *
import os

async def create_product(session:AsyncSession,product_create:ProductCreate)->HTTPAnswer:
    product = await get_product_by_name(name=product_create.name,session=session)
    if product:
        return {'detail':'already exists'}
    product=Product(**product_create.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return {'detail':'success'}

async def update_product_picture(session:AsyncSession,name:str,picture:UploadFile)->HTTPAnswer:
    if not picture:
        return {"detail":"no picture"}
    
    product = await get_product_by_name(session=session,name=name)

    if not product:
        return {"detail":"no product"}
    
    if product.picture:
        os.remove('media/'+product.picture)

    path=f'{product.name.lower()}.webp'
    product.picture=path

    with open("media/"+path,"wb+") as buff:
        buff.write(picture.file.read())

    await session.commit()
    return {'detail':"success"}


async def get_all_products(session:AsyncSession)->Sequence[Product]:
    result = await session.scalars(select(Product))
    return result.all()

async def get_product_by_id(session:AsyncSession,id:int)->Product:
    query=select(Product).where(Product.id==id)
    result = await session.execute(query)
    return result.scalars().first()

async def get_product_by_name(session:AsyncSession,name:str)->Product:
    query=select(Product).where(Product.name==name)
    result=await session.execute(query)
    return result.scalars().first()

async def update_product_price(session:AsyncSession,name:str,price:int)->HTTPAnswer:
    product=await get_product_by_name(session=session,name=name)
    if product is None:
        return {'detail':'no such index'}
    product.price=price
    await session.commit()
    await session.refresh(product)
    return {'detail':'success'}

async def delete_product_by_id(session:AsyncSession,id:int)->HTTPAnswer:
    product = await get_product_by_id(session=session,id=id)
    if product is not None:
        query=delete(Product).where(Product.id==id)
        await session.execute(query)
        await session.commit()
        return {'detail':'success'}
    return {'detail':'not found'}

