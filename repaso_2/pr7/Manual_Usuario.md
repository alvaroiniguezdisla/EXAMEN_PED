# Manual de Usuario

Este manual explica cómo ejecutar y usar la aplicación de chat cliente‑servidor.

---

## Requisitos previos

* Tener los ejecutables `serv7` y `cli7` generados (ver Manual de Instalación).

---

## 1. Iniciar el servidor


./serv7


* Escucha en **0.0.0.0:4000**.
* Para detenerlo: pulsa **Ctrl + C**.

---

## 2. Conectar un cliente


./cli7 <host> <puerto>


* `<host>`: IP o nombre de la máquina con el servidor.
* `<puerto>`: por defecto **4000**.
* Ejemplo: `./cli7 127.0.0.1 4000`

---

## 3. Autenticación

1. El cliente pide:


   Introduce tu nick:
   
2. Escribe un **nick** (sin espacios) y pulsa Enter.
3. Si está libre, verás:


   OK
   --- Conectado. Escribe mensajes o /quit para salir. ---


---

## 4. Uso del chat

* Envía mensajes escribiendo texto y pulsando Enter.
* Para desconectarte:

  * Escribe `/quit` y pulsa Enter, o
  * Pulsa **Ctrl + D**.

---

## 5. Notificaciones del sistema

* Al conectarse o desconectarse otro usuario:


  * usuario se ha conectado
  * usuario se ha desconectado

* Si el servidor se cierra:


  * SERVIDOR detenido, bye


---

## Opciones de configuración

* Para cambiar el puerto del servidor, edita la variable `PORT` en `serv7.py` y vuelve a generar el ejecutable con `make serv7`.
* El cliente siempre requiere `<host>` y `<puerto>` al invocarlo (`./cli7 <host> <puerto>`).
