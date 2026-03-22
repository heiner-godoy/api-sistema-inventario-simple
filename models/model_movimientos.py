from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from config.connection import Base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Movimiento(Base):
    __tablename__ = 'movimientos'

    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    tipo = Column(String(50), nullable=False)
    cantidad = Column(Integer, nullable=False)
    descripcion = Column(String(255))
    fecha = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    producto = relationship('Producto', back_populates='movimientos')
