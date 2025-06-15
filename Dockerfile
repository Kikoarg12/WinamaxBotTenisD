FROM python:3.10-slim

# Instala dependencias necesarias del sistema para Playwright
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    fonts-liberation \
    libnss3 \
    libatk-bridge2.0-0 \
    libxss1 \
    libasound2 \
    libgbm1 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# Instala Playwright y sus navegadores
RUN pip install playwright
RUN playwright install --with-deps

# Copia los archivos del proyecto
WORKDIR /app
COPY . .

# Instala dependencias Python del proyecto
RUN pip install -r requirements.txt

# Comando para iniciar el bot
CMD ["python", "main.py"]
