FROM python:3.10-slim

# Instala dependencias necesarias del sistema para Playwright
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    fonts-liberation \
    libnss3 \
    libatk-bridge2.0-0 \
    libxss1 \
    libasound2 \
    libgbm1 \
    libgtk-3-0 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Crea y selecciona el directorio de trabajo
WORKDIR /app

# Copia todos los archivos del proyecto
COPY . .

# Instala las dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Instala los navegadores de Playwright mediante script externo
COPY build.sh .
RUN chmod +x build.sh && ./build.sh

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
