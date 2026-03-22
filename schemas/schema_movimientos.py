from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class CrearMovimiento(BaseModel):
    producto_id: int = Field(..., description="ID del producto")
    cantidad: int = Field(..., gt=0, description="Cantidad del movimiento")
    tipo: str = Field(..., description="Tipo de movimiento (entrada o salida)")
    descripcion: Optional[str] = Field(None, description="Descripción del movimiento")

class ResponseMovimiento(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_movimiento: int = Field(..., description="ID del movimiento")
    producto_id: int = Field(..., description="ID del producto")
    cantidad: int = Field(..., description="Cantidad del movimiento")
    tipo: str = Field(..., description="Tipo de movimiento (entrada o salida)")
    descripcion: Optional[str] = Field(None, description="Descripción del movimiento")
    fecha: datetime = Field(..., description="Fecha y hora del movimiento")