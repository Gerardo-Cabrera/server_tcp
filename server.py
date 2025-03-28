import socket

def iniciar_servidor():
    HOST = 'localhost'
    PORT = 5000
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor escuchando en {HOST}:{PORT}...")
        
        try:
            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Conexión establecida desde {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        mensaje = data.decode().strip()
                        print(f"Cliente envía: {mensaje}")
                        
                        if mensaje.upper() == "DESCONEXION":
                            print(f"Solicitud de desconexión de {addr}")
                            break

                        if mensaje.lower() == "hola servidor":
                            respuesta = "HOLA CLIENTE"
                        else:
                            respuesta = mensaje.upper()
                        
                        conn.sendall(respuesta.encode())
                        print(f"Servidor responde: {respuesta}")
                        
                    print("Servidor cierra la conexión con el cliente.")
        except KeyboardInterrupt:
            print("\nServidor detenido")

if __name__ == "__main__":
    iniciar_servidor()
