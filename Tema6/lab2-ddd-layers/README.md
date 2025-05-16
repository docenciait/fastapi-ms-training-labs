# Lab 2 - Capas DDD con Arquitectura Hexagonal

Este laboratorio muestra cómo estructurar una aplicación siguiendo las capas DDD:
- Dominio
- Aplicación
- Infraestructura
- Interfaces

## 🧱 Estructura

```
app/
├── domain/
│   └── entities/
│       └── user.py
├── application/
│   ├── ports/
│   │   └── user_repository.py
│   └── use_cases/
│       └── list_users.py
├── infrastructure/
│   └── repositories/
│       └── in_memory_user_repo.py
├── interfaces/
│   └── routes/
│       └── users.py
└── main.py
```

## ▶️ Cómo ejecutar

```bash
docker-compose up --build
```

Visita: [http://localhost:8000/users](http://localhost:8000/users)

## 📚 Conceptos Aplicados

- Separación estricta por capas de DDD
- Repositorio como puerto de salida
- Caso de uso como servicio de aplicación
- Adaptador HTTP como entrada