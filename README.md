# 📦 Sistema de Inventario

API REST para la gestión de productos, categorías y movimientos de inventario.

---

## 🚀 Tecnologías

- **Python 3.13**
- **FastAPI** — framework web
- **SQLAlchemy** — ORM
- **Alembic** — migraciones de base de datos
- **PostgreSQL** — base de datos
- **Pydantic** — validación de datos
- **JWT (python-jose)** — autenticación
- **Passlib + bcrypt** — hash de contraseñas
- **Uvicorn** — servidor ASGI

---

## 📁 Estructura del proyecto

```
inventario-backend/
├── alembic/                  # Migraciones de base de datos
│   ├── versions/
│   └── env.py
├── config/
│   ├── connection.py         # Configuración de la base de datos
│   └── settings.py          # Variables de entorno
├── controllers/              # Endpoints de cada módulo
│   ├── controller_auth.py
│   ├── controller_categorias.py
│   ├── controller_productos.py
│   └── controller_movimientos.py
├── middlewares/
│   ├── auth.py              # Middleware de autenticación JWT
│   └── cors.py              # Configuración de CORS
├── models/                   # Modelos de base de datos
│   ├── model_categorias.py
│   ├── model_productos.py
│   └── model_movimientos.py
├── routes/                   # Registro de routers
│   ├── router_auth.py
│   ├── router_categorias.py
│   ├── router_productos.py
│   └── router_movimientos.py
├── schemas/                  # Schemas de validación
│   ├── schema_categorias.py
│   ├── schema_productos.py
│   └── schema_movimientos.py
├── services/                 # Lógica de negocio
│   ├── service_categorias.py
│   ├── service_productos.py
│   └── service_movimientos.py
├── utils/
│   ├── security.py          # Hash de contraseñas
│   └── jwt.py               # Generación de tokens JWT
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
├── main.py
└── requirements.txt
```

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git https://github.com/heiner-godoy/api-sistema-inventario-simple.git
cd inventario-backend
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
cp .env.example .env
```

```env
DATABASE_URL=postgresql://postgres:tu_password@localhost:5432/inventario
SECRET_KEY=tu_clave_secreta_larga_y_aleatoria
DEBUG=False
ALLOWED_HOSTS=localhost
```

Para generar una `SECRET_KEY` segura:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Crear la base de datos en PostgreSQL

```sql
CREATE DATABASE inventario;
```

### 6. Ejecutar las migraciones

```bash
alembic upgrade head
```

### 7. Iniciar el servidor

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`

---

## 📖 Documentación

- **Swagger UI** → `http://127.0.0.1:8000/docs`
- **ReDoc** → `http://127.0.0.1:8000/redoc`

---

## 🔐 Autenticación

La API usa **JWT Bearer Token**:

```http
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=correo@ejemplo.com&password=tu_contraseña
```

Respuesta:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

## 📌 Endpoints

### Auth
| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| POST | `/auth/login` | Iniciar sesión | No |

### Categorías
| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| GET | `/categorias/` | Listar categorías | No |
| GET | `/categorias/{id}` | Obtener categoría | No |
| POST | `/categorias/` | Crear categoría | Sí |

### Productos
| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| GET | `/productos/` | Listar productos | No |
| GET | `/productos/{id}` | Obtener producto | No |
| POST | `/productos/` | Crear producto | Sí |
| PUT | `/productos/{id}` | Actualizar producto | Sí |
| DELETE | `/productos/{id}` | Eliminar producto | Sí |

### Movimientos
| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| GET | `/movimientos/` | Listar movimientos | No |
| GET | `/movimientos/{id}` | Obtener movimiento | No |
| POST | `/movimientos/` | Registrar movimiento | Sí |

---

## 📊 Modelo de datos

```
CATEGORIAS
├── id_categoria (PK)
└── nombre

PRODUCTOS
├── id_producto (PK)
├── id_categoria (FK → CATEGORIAS)
├── nombre
├── descripcion
├── precio
└── stock

MOVIMIENTOS
├── id_movimiento (PK)
├── id_producto (FK → PRODUCTOS)
├── tipo          → "entrada" o "salida"
├── cantidad
├── fecha
└── descripcion
```

---

## ⚠️ Reglas de negocio

- Al registrar una **salida**, el sistema verifica que `stock >= cantidad`
- Si no hay suficiente stock retorna error `400`
- Al registrar una **entrada**, el stock se incrementa automáticamente
- Al registrar una **salida**, el stock se decrementa automáticamente
- No se puede eliminar una categoría que tenga productos asociados

---

## 🗄️ Migraciones

```bash
# Crear nueva migración
alembic revision --autogenerate -m "descripcion del cambio"

# Aplicar migraciones
alembic upgrade head

# Revertir última migración
alembic downgrade -1
```

---

## 🔒 Seguridad

- Contraseñas hasheadas con **bcrypt**
- Tokens JWT con expiración de **60 minutos**
- Endpoints de escritura protegidos con JWT
- Nunca subas el archivo `.env` a Git

---

## 📦 Dependencias principales

```
fastapi
uvicorn[standard]
sqlalchemy
alembic
psycopg2-binary
pydantic
python-decouple
python-jose[cryptography]
passlib[bcrypt]
python-multipart
```

---

## 👨‍💻 Autor

Desarrollado por **Heiner Godoy**
