from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.connection import get_db
from schemas.schema_movimientos import MovimientoCreate, ResponseMovimiento
from services.service_movimientos import get_movimientos, get_movimiento, create_movimiento

router = APIRouter(prefix="/movimientos", tags=["Movimientos"])

@router.get("/", response_model=list[ResponseMovimiento])
def list_movimientos(db: Session = Depends(get_db)):
    return get_movimientos(db)

@router.get("/{movimiento_id}", response_model=ResponseMovimiento)
def get_movimiento_by_id(movimiento_id: int, db: Session = Depends(get_db)):
    movimiento = get_movimiento(db, movimiento_id)
    if not movimiento:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return movimiento

@router.post("/", response_model=ResponseMovimiento, status_code=201)
def add_movimiento(movimiento: MovimientoCreate, db: Session = Depends(get_db)):
    try:
        return create_movimiento(db, movimiento)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))




