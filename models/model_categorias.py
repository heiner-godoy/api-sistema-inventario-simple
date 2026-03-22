from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.connection import Base

class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(200), nullable=True)

    productos = relationship('Producto', back_populates='categoria')