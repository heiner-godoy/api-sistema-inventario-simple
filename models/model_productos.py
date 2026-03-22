from sqlalchemy import column, Integer, String, ForeignKey, text
from config.connection import Base
from sqlalchemy.orm import relationship

class Producto(Base):
    __tablename__ = 'productos'

    id = column(Integer, primary_key=True)
    id_categoria = column(Integer, ForeignKey('categorias.id'), nullable=False)
    nombre = column(String(100), nullable=False)
    descripcion = column(text(255), nullable=True)
    precio = column(float, nullable=False)
    categoria_id = column(Integer, ForeignKey('categorias.id'), nullable=False)
    stock = column(Integer, nullable=False)

    id_categoria = relationship('Categoria', back_populates='productos')


