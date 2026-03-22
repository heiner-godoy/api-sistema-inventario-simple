from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.connection import get_db 
from schemas.schema_productos import ProductoCreate, ProductoUpdate, ResponseProducto
from services.service_productos import create_producto, get_productos, get_producto, update_producto, delete_producto

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/", response_model=list[ResponseProducto])
def list_productos(db: Session = Depends(get_db)):
    return get_productos(db)

@router.get("/{producto_id}", response_model=ResponseProducto)
def get_producto_by_id(producto_id: int, db: Session = Depends(get_db)):
    producto = get_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/", response_model=ResponseProducto, status_code=201)
def add_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    try:
        return create_producto(db, producto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{producto_id}", response_model=ResponseProducto)
def update_producto_by_id(producto_id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    updated_producto = update_producto(db, producto_id, producto)
    if not updated_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated_producto

@router.delete("/{producto_id}", status_code=204)
def delete_producto_by_id(producto_id: int, db: Session = Depends(get_db)):
    deleted = delete_producto(db, producto_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return None