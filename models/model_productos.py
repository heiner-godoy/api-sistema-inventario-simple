from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from config.connection import Base
from sqlalchemy.orm import relationship

class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True)
    id_categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)

    categoria = relationship('Categoria', back_populates='productos')
    movimientos = relationship('Movimiento', back_populates='producto')