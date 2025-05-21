# Manual de Instalación (¡Muy sencillo!)

Sigue estos pasos como si fuera un tutorial para principiantes.



## 1. ¿Qué necesitas?

* **Python 3** instalado (cualquiera de las versiones modernas funciona).
* Los dos archivos en la misma carpeta:

  * `serv7.py` (servidor)
  * `cli7.py` (cliente)
* (Opcional) **make** para automatizar: si no lo tienes, usa los comandos manuales.

---

## 2. Dar permisos de ejecución

1. Abre una **terminal** (o consola) en la carpeta donde están los archivos.
2. Escribe y ejecuta:


   chmod +x serv7.py cli7.py


   Esto permite que tu sistema pueda “correr” esos programas.

---

## 3. Crear los programas ejecutables

*Si tienes `make`, haz esto:*


make serv7   # crea un archivo llamado serv7
make cli7    # crea un archivo llamado cli7


*Si NO tienes `make`, hazlo manualmente así:*


cp serv7.py serv7   # copia y renombra el servidor
cp cli7.py cli7     # copia y renombra el cliente
chmod +x serv7 cli7 # dale permiso para ejecutar


---

## 4. Probar que todo existe

En la terminal, escribe:


ls -l serv7 cli7


Deberías ver dos archivos con permisos de ejecución (`-rwxr-xr-x`).

---

## 5. Cambiar el puerto (si quieres)

Por defecto, el servidor usa el **puerto 4000**. Si quieres otro, edita la línea `PORT = 4000` en `serv7.py` y luego repite el paso 3 (crear ejecutables con `make` o con `cp`).

---

## 6. ¡Listo para usar!

Continúa con el **Manual de Usuario** para aprender a arrancar el servidor y los clientes.
