from sqlalchemy import Column, Integer, String
from config.connection import Base

class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)

