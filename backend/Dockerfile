# Dockerfile
FROM python:3.11-slim

# Evita prompts y reduce tamaño
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependencias necesarias del sistema
RUN apt-get update && apt-get install -y build-essential gcc libssl-dev libffi-dev curl \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# Crea el directorio de la app
WORKDIR /app

# Copia requirements e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu código
COPY ./app ./app

# Expone el puerto que usará Uvicorn
EXPOSE 8000

# Comando para iniciar FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
