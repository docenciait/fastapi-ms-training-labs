# Lab 1 - Patrón Puertos y Adaptadores (Hexagonal)

Este laboratorio introduce el patrón de arquitectura hexagonal (puertos y adaptadores) utilizando FastAPI.

## 🧱 Estructura

```
app/
├── domain/             # Entidades del dominio
│   └── user.py
├── application/        # Interfaces de los puertos (input/output)
│   └── ports.py
├── infrastructure/     # Adaptadores de salida (repositorio en memoria)
│   └── repository.py
├── interfaces/         # Adaptadores de entrada (API HTTP)
│   └── http.py
└── main.py             # Entrada principal de la app
```

## ▶️ Cómo ejecutar

### Requisitos

- Docker y Docker Compose

### Pasos

```bash
docker-compose up --build
```

Visita: [http://localhost:8000/users](http://localhost:8000/users)

Deberías ver:

```json
[
  {
    "id": 1,
    "name": "Alice"
  },
  {
    "id": 2,
    "name": "Bob"
  }
]
```

## 📚 Conceptos Aplicados

- Arquitectura Hexagonal
- Separación de capas
- Puerto de salida (UserRepository)
- Adaptador de entrada (FastAPI)
- Adaptador de salida (InMemoryUserRepository)