from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class CategoriaCreate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50, description="Nombre de la categoría")
    descripcion: Optional[str] = Field(None, min_length=2, max_length=200, description="Descripción de la categoría")

class ResponseCategoria(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., description="ID de la categoría")
    nombre: str = Field(..., description="Nombre de la categoría")
    descripcion: Optional[str] = Field(None, description="Descripción de la categoría")
    
class CategoriaUpdate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50, description="Nombre de la categoría")
    descripcion: Optional[str] = Field(None, min_length=2, max_length=200, description="Descripción de la categoría")


