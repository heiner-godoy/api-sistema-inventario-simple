from sqlalchemy.orm import Session
from models.model_productos import Producto
from schemas.schema_productos import CrearProducto, ProductoUpdate

def get_productos(db: Session):
    return db.query(Producto).all()

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def create_producto(db: Session, producto: CrearProducto):
    db_producto = Producto(categoria_id=producto.categoria_id,
                            nombre=producto.nombre, 
                            descripcion=producto.descripcion,
                            precio=producto.precio,
                            stock=producto.stock)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def update_producto(db: Session, producto_id: int, producto: ProductoUpdate):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if db_producto is None:
        return None
    if producto.categoria_id is not None:
        db_producto.categoria_id = producto.categoria_id
    if producto.nombre is not None:
        db_producto.nombre = producto.nombre
    if producto.descripcion is not None:
        db_producto.descripcion = producto.descripcion
    if producto.precio is not None:
        db_producto.precio = producto.precio
    if producto.stock is not None:
        db_producto.stock = producto.stock
    db.commit()
    db.refresh(db_producto)
    return db_producto

def delete_producto(db: Session, producto_id: int):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if db_producto is None:
        return None
    db.delete(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

