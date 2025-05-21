# Makefile sencillo para serv7/cli7
PYTHON     = python3
HOST ?= localhost
PORT ?= 4000

.PHONY: serv7 cli7 clean

# Crea el ejecutable 'serv7' apuntando a serv7.py
serv7: serv7.py
	chmod +x $<
	ln -sf $< serv7

# Crea el ejecutable 'cli7' apuntando a cli7.py
cli7: cli7.py
	chmod +x $<
	ln -sf $< cli7

# Limpia los enlaces serv7 y cli7
clean:
	rm -f serv7 cli7
