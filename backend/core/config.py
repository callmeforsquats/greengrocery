from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class RunConfig(BaseModel):
    host:str="0.0.0.0"
    port:int=8000

class ApiConfig(BaseModel):
    prefix:str="/api"

class DbConfig(BaseModel):
    url:str="postgresql+asyncpg://postgres:111@localhost:5432/greengrocery"
    pool_size:int=50
    max_overflow:int=50
    echo:bool=True

class Settings(BaseSettings):
    model_config=SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix="app__",
        env_file=".env",
        env_file_encoding="utf-8"
    )
    run:RunConfig=RunConfig()
    api:ApiConfig=ApiConfig()
    db:DbConfig=DbConfig()

settings=Settings()