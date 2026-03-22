from fastapi import APIRouter
from controllers.controller_movimientos import router as MovimientosController

Movimientos_router = APIRouter()
Movimientos_router.include_router(MovimientosController)