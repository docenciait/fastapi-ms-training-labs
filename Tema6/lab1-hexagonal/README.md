# Lab 1 - Patrón Hexagonal con MariaDB

Este laboratorio implementa una arquitectura hexagonal usando FastAPI y MariaDB como fuente de datos persistente.

## ▶️ Ejecutar

```bash
docker-compose up --build
```

Visita: [http://localhost:8000/users](http://localhost:8000/users)

## 🧱 Estructura

- `core`: modelos de dominio
- `adapters/outbound`: acceso a la base de datos
- `adapters/inbound`: rutas HTTP (controladores)
- `config`: configuración de base de datos

## 🗄️ Datos de ejemplo

Se cargan automáticamente al iniciar MariaDB:

```sql
INSERT INTO users (name) VALUES ('Alice'), ('Bob');
```