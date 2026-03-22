from sqlalchemy.orm import Session
from models.model_categorias import Categoria
from schemas.schema_categorias import CategoriaCreate, CategoriaUpdate, CategoriaUpdate

def get_categorias(db: Session):
    return db.query(Categoria).all()

def get_categoria(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def create_categoria(db: Session, categoria: CategoriaCreate):
    db_categoria = Categoria(nombre=categoria.nombre, 
                            descripcion=categoria.descripcion)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def update_categoria(db: Session, categoria_id: int, categoria: CategoriaUpdate):
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if db_categoria is None:
        return None
    db_categoria.nombre = categoria.nombre
    db_categoria.descripcion = categoria.descripcion
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, categoria_id: int):
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if db_categoria is None:
        return None
    db.delete(db_categoria)
    db.commit()
    return db_categoria