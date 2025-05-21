.PHONY: serv6 cli6 test clean all

# Variables de configuración por defecto
PORT ?= 5006
HOST ?= 127.0.0.1

# Ejecutar servidor
serv6:
	python3 serv6.py $(PORT)

# Ejecutar cliente
cli6:
	python3 cli6.py $(HOST) $(PORT)

# Ejecutar tests unitarios TDD
test:
	python3 -m unittest tests

# Compilación general (placeholder)
all:
	@echo "Compilación lista. Usa 'make test' para ejecutar los tests o 'make serv6/cli6' para sockets."

# Limpieza de archivos temporales
clean:
	@echo "Limpiando archivos .pyc y __pycache__..."
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -r {} +
