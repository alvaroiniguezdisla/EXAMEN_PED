# Documento de Arquitectura

Este documento describe la arquitectura de la aplicación de chat cliente-servidor.

---

## 1. Componentes Principales

| Componente             | Descripción                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Servidor** (`serv7`) | Se encarga de aceptar conexiones, gestionar nicks únicos, recibir y reenviar mensajes a todos los clientes. Implementado en Python usando `socket` y `select`. |
| **Cliente** (`cli7`)   | Se conecta al servidor, envía el nick, envía y recibe mensajes en tiempo real. Implementado en Python usando `socket` y `select`.                              |

---

## 2. Estructuras de Datos

* **clients** (lista): contiene el socket de escucha y los sockets de todos los clientes conectados.
* **nicknames** (diccionario): mapea cada socket de cliente a su nick (cadena de texto).

---

## 3. Flujo de Conexión y Mensajes

1. **Inicio del servidor**:

   1. Crear socket TCP (`AF_INET`, `SOCK_STREAM`).
   2. `bind()` a `0.0.0.0:PORT` y `listen()`.
   3. Añadir el socket de escucha a `clients`.

2. **Aceptación de clientes**:

   1. `select()` detecta actividad en el socket de escucha.
   2. `accept()` -> nuevo socket de cliente.
   3. El cliente envía su `nick` (primera línea).
   4. El servidor comprueba unicidad en `nicknames`.
   5. Si está libre: envía `OK\n`, añade socket a `clients` y `nicknames`.
   6. Si no: envía `ERROR: nick en uso\n` y cierra la conexión.

3. **Intercambio de mensajes**:

   1. `select()` detecta datos en sockets de clientes.
   2. `recv()` lee el mensaje (texto + `\n`).
   3. Construye `nick: mensaje`.
   4. Reenvía a todos los clientes mediante `broadcast_message()`.

4. **Desconexión**:

   * Si `recv()` devuelve 0 o hay error, se llama a `disconnect_client()`, que:

     1. Notifica a todos con `* nick se ha desconectado`.
     2. Quita socket de `clients` y `nicknames`, y cierra el socket.

5. **Parada del servidor**:

   * Captura `SIGINT` (Ctrl-C).
   * Envía `* SERVIDOR detenido, bye` a todos los clientes.
   * Cierra todos los sockets y termina el proceso.

---

## 4. Protocolo de Aplicación

* **Registro**: el cliente envía su nick seguido de `\n`.
* **Confirmación**: servidor responde `OK\n` o `ERROR: motivo\n`.
* **Mensajes**: cada línea enviada se rebroadcast como `nick: texto\n`.
* **Notificaciones**: conexión/desconexión de usuarios y parada del servidor.

---

## 5. Concurrencia y Selección

* Se emplea la llamada `select()` para multiplexar E/S en un único hilo.
* Permite atender múltiples clientes sin bloquearse.

---

## 6. Extensiones Futuras

* Soporte de canales (temas).
* Almacenamiento de histórico de conversaciones.
* Autenticación y cifrado.
* Pasar el servidor a demonio o servicio del sistema.
