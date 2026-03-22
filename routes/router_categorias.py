from fastapi import APIRouter
from controllers.controller_categorias import router as CategoriasController


Categorias_router = APIRouter()
Categorias_router.include_router(CategoriasController)
