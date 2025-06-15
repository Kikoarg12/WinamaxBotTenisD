#!/bin/bash
set -e

# Instala navegadores necesarios para Playwright
echo "🔧 Instalando navegadores de Playwright..."
playwright install --with-deps
