# Laboratorio 1: Análisis del Monolito y Estrategia de Descomposición

## Objetivos de Aprendizaje

Al finalizar este laboratorio, serás capaz de:
* Comprender la estructura y funcionalidades de una aplicación FastAPI monolítica de ejemplo ("ECommercePlatform").
* Identificar los límites de los contextos de negocio (Bounded Contexts) dentro del monolito.
* Evaluar diferentes estrategias para la descomposición de monolitos.
* Proponer y documentar los microservicios candidatos a ser extraídos.
* Seleccionar el primer microservicio a extraer y justificar la elección.

## Contexto


## 📋 Enunciado

En este laboratorio partimos de un **monolito FastAPI** llamado **ECommercePlatform** que gestiona **Usuarios**, **Productos** y **Pedidos** en memoria. Nuestro objetivo es:

1. Comprender la estructura y funcionamiento del monolito.
2. Identificar los **Bounded Contexts** (Usuarios, Productos, Pedidos).
3. Proponer y justificar una estrategia de descomposición.
4. Extraer el monolito en **dos microservicios** independientes:
   - **User Service** (puerto 8000)
   - **Product Service** (puerto 8001)

Al final deberás tener funcionando cada servicio por separado, tanto con **uvicorn + pipenv** como con **Docker** o **Docker Compose**.

---

## 🏗️ Estructura de Directorios

```text
lab01-microservices/
├─ user-service/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ routers/users.py
│  │  ├─ models/user.py
│  │  └─ db/memory_db.py
│  ├─ Pipfile
│  ├─ Pipfile.lock
│  └─ Dockerfile
├─ product-service/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ routers/products.py
│  │  ├─ models/product.py
│  │  └─ db/memory_db.py
│  ├─ Pipfile
│  ├─ Pipfile.lock
│  └─ Dockerfile
└─ docker-compose.yml
```



---



## 🚀 Ejecución con Uvicorn + Pipenv 


### Prerrequisitos 

 
- Python ≥ 3.11
 
- [pipenv](https://pipenv.pypa.io/)


### Pasos (por servicio) 

 
2. **Clona o descomprime**  el repositorio y ve al directorio del servicio:


```bash
cd user-service
```
 
4. **Crear el entorno**  y **instalar dependencias** :


```bash
pipenv --python 3.10
pipenv install fastapi uvicorn pydantic
```
 
6. **Entrar al shell**  de Pipenv:


```bash
pipenv shell
```
 
8. **Arrancar con Uvicorn** :


```bash
uvicorn app.main:app --reload --port 8000
```


> El servicio de usuarios quedará disponible en `http://localhost:8000/docs`.
 
10. Repite los mismos pasos en `product-service/`, sustituyendo el puerto a `8001`:


```bash
cd ../product-service
pipenv --python 3.10
pipenv install fastapi uvicorn pydantic
pipenv shell
uvicorn app.main:app --reload --port 8001
```


> `http://localhost:8001/docs`



---



## 🐳 Ejecución con Docker 

Cada servicio trae su propio **Dockerfile** . Desde la carpeta de cada uno:


```bash
# User Service
cd user-service
docker build -t user-service .
docker run -d --name user-service -p 8000:8000 user-service

# Product Service
cd ../product-service
docker build -t product-service .
docker run -d --name product-service -p 8001:8001 product-service
```



---



## ⚓ Ejecución con Docker Compose 

En la raíz (`lab01-microservices/`) crea un archivo `docker-compose.yml`:


```yaml
version: "3.8"

services:
  user-service:
    build: ./user-service
    container_name: user-service
    ports:
      - "8000:8000"
    restart: unless-stopped

  product-service:
    build: ./product-service
    container_name: product-service
    ports:
      - "8001:8001"
    restart: unless-stopped
```


### Arranque 



```bash
docker-compose up --build -d
```

 
- **User Service**  en `http://localhost:8000/docs`
 
- **Product Service**  en `http://localhost:8001/docs`


Para detener:



```bash
docker-compose down
```



---



## 📝 Estrategia de Descomposición 

 
2. **Bounded Contexts** 
 
  - **Usuarios** : gestión de cuentas y autenticación.
 
  - **Productos** : catálogo y precios.
 
4. **Criterios de extracción** 
 
  - **Independencia** : mínimo acoplamiento entre contextos.
 
  - **Escalabilidad** : catálogo de productos crece a distinta velocidad.
 
  - **Valor de negocio** : cada equipo puede iterar por separado.
 
6. **Patrón Strangler Fig** 
 
  - Se extraen servicios uno a uno conviviendo con el monolito.
 
  - Empezamos por **User Service** , luego **Product Service** , y en siguientes labs añadiríamos **Order Service** .



---
