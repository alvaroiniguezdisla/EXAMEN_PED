.PHONY: test servidor cliente clean all

# Configuración del puerto (ajusta según tu grupo)
PUERTO=16052
HOST=127.0.0.1

# Ejecutar tests unitarios
test:
	python3 -m unittest tests

# Ejecutar servidor
servidor:
	python3 servidor.py

# Ejecutar cliente
cliente:
	python3 cliente.py

# Limpieza de archivos temporales
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -r {} +

# Placeholder para futuras tareas
all:
	@echo "Usa 'make test', 'make servidor' o 'make cliente'."
