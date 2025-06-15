FROM python:3.10-slim

# Instala dependencias del sistema necesarias para Playwright
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

# Instala Playwright y navegadores
RUN pip install playwright && playwright install chromium

# Copia los archivos del proyecto
WORKDIR /app
COPY . .

# Instala dependencias Python
RUN pip install -r requirements.txt

# Comando de ejecución
CMD ["python", "main.py"]
