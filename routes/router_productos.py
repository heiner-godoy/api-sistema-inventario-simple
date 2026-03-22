from fastapi import APIRouter
from controllers.controller_productos import router as ProductosController

Productos_router = APIRouter()
Productos_router.include_router(ProductosController)

