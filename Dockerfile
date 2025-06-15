FROM python:3.10-slim

# Instalación de dependencias del sistema
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    libnss3 \
    libatk-bridge2.0-0 \
    libxss1 \
    libasound2 \
    libgbm1 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# Instala Playwright + navegadores
RUN pip install playwright \
    && playwright install --with-deps chromium

# Copia el código
WORKDIR /app
COPY . .

# Instala requirements (por si lo tienes aparte)
RUN pip install -r requirements.txt

# Ejecuta tu script
CMD ["python", "main.py"]
