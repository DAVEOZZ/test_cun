
# Usa la imagen base de Python para FastAPI
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el código de la aplicación al contenedor
COPY . .

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que FastAPI va a ejecutarse
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "presentation.api:app", "--host", "0.0.0.0", "--port", "8000"]

