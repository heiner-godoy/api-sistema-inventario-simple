from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.connection import get_db
from schemas.schema_categorias import CategoriaCreate, CategoriaUpdate, ResponseCategoria
from services.service_categorias import get_categorias, get_categoria, create_categoria, update_categoria, delete_categoria

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("/", response_model=list[ResponseCategoria])
def list_categorias(db: Session = Depends(get_db)):
    return get_categorias(db)

@router.get("/{categoria_id}", response_model=ResponseCategoria)
def get_categoria_by_id(categoria_id: int, db: Session = Depends(get_db)):
    categoria = get_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria

@router.post("/", response_model=ResponseCategoria, status_code=201)
def add_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    try:
        return create_categoria(db, categoria)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{categoria_id}", response_model=ResponseCategoria)
def update_categoria_by_id(categoria_id: int, categoria: CategoriaUpdate, db: Session = Depends(get_db)):
    updated_categoria = update_categoria(db, categoria_id, categoria)
    if not updated_categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return updated_categoria

@router.delete("/{categoria_id}", status_code=204)
def delete_categoria_by_id(categoria_id: int, db: Session = Depends(get_db)):
    deleted = delete_categoria(db, categoria_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return None
