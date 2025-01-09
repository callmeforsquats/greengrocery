from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    name:str
    price:int
    description:str


class ProductCreate(ProductBase):
    pass 

class ProductRead(ProductBase):
    id:int
    picture:str

class HTTPAnswer(BaseModel):
    detail:str
    model_config=ConfigDict(json_schema_extra={'detail':'HTTPException raised'})
