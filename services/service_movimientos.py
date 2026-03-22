from sqlalchemy.orm import Session
from models.model_movimientos import Movimiento
from models.model_productos import Producto
from schemas.schema_movimientos import MovimientoCreate, MovimientoUpdate

def get_movimientos(db: Session):
    return db.query(Movimiento).all()

def get_movimiento(db: Session, movimiento_id: int):
    return db.query(Movimiento).filter(Movimiento.id == movimiento_id).first()

def create_movimiento(db: Session, movimiento: MovimientoCreate):
    producto = db.query(Producto).filter(Producto.id == movimiento.producto_id).first()

    if not producto:
        raise ValueError("Producto no encontrado")

    if movimiento.tipo == "salida":
        if producto.stock < movimiento.cantidad:
            raise ValueError(f"Stock insuficiente. Stock actual: {producto.stock}")
        producto.stock -= movimiento.cantidad

    elif movimiento.tipo == "entrada":
        producto.stock += movimiento.cantidad

    else:
        raise ValueError("Tipo inválido. Use 'entrada' o 'salida'")

    db_movimiento = Movimiento(
        producto_id=movimiento.producto_id,
        cantidad=movimiento.cantidad,
        tipo=movimiento.tipo,
        descripcion=movimiento.descripcion
    )
    db.add(db_movimiento)
    db.commit()
    db.refresh(db_movimiento)
    return db_movimiento

def update_movimiento(db: Session, movimiento_id: int, movimiento: MovimientoUpdate):
    db_movimiento = db.query(Movimiento).filter(Movimiento.id == movimiento_id).first()
    if db_movimiento is None:
        return None
    if movimiento.producto_id is not None:
        db_movimiento.producto_id = movimiento.producto_id
    if movimiento.cantidad is not None:
        db_movimiento.cantidad = movimiento.cantidad
    if movimiento.tipo is not None:
        db_movimiento.tipo = movimiento.tipo
    if movimiento.descripcion is not None:
        db_movimiento.descripcion = movimiento.descripcion
    db.commit()
    db.refresh(db_movimiento)
    return db_movimiento