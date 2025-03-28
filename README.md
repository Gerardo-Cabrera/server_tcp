# Servidor y Cliente TCP

Implementación de un servidor y cliente TCP que se comunican en "localhost" a través el puerto "5000" (localhost:5000).

## Requisitos
- Python 3.x

## Instrucciones de Ejecución

### 1. **Ejecutar Servidor**

Abrir una terminal y ejecutar:
```bash
python server.py
```

Abrir otra terminal y ejecutar:
```bash
python client.py
```

# Pruebas Manuales

## Prueba 1: Mensaje Normal
1. En cliente, ingresar por ejemplo: "hola servidor" u "hola mundo"
2. Verificar que el servidor responda: "HOLA CLIENTE" u "HOLA MUNDO"

## Prueba 2: Desconexión
1. En el cliente, ingresar: "DESCONEXION"
2. Verificar que el cliente se desconecta.
3. Verificar que el servidor mantiene su ejecución.
4. Verificar que un nuevo cliente se pueda conectar.