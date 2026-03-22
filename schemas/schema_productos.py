from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class CrearProducto(BaseModel):
    categoria_id: int = Field(..., description="ID de la categoría")
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre del producto")
    descripcion: Optional[str] = Field(None, description="Descripción del producto")
    precio: float = Field(..., gt=0, description="Precio del producto")
    stock: int = Field(..., ge=0, description="Stock inicial del producto")

class ResponseProducto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., description="ID del producto")
    categoria_id: int = Field(..., description="ID de la categoría")
    nombre: str = Field(..., description="Nombre del producto")
    descripcion: Optional[str] = Field(None, description="Descripción del producto")
    precio: float = Field(..., description="Precio del producto")
    stock: int = Field(..., description="Stock del producto")
