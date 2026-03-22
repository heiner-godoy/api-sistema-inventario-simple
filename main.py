from fastapi import FastAPI
from routes.router_categorias import Categorias_router
from routes.router_productos import Productos_router
from routes.router_movimientos import Movimientos_router


app = FastAPI(title="My FastAPI Application")
app.include_router(Categorias_router)
app.include_router(Productos_router)
app.include_router(Movimientos_router)