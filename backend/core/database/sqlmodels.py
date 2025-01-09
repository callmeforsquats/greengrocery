from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    __abstract__=True
    id:Mapped[int]=mapped_column(primary_key=True)

class Product(Base):
    __tablename__="products"
    name:Mapped[str]=mapped_column(unique=True)
    price:Mapped[int]=mapped_column(server_default="0",nullable=False)
    description:Mapped[str]=mapped_column(nullable=True)
    picture:Mapped[str]=mapped_column(nullable=True)