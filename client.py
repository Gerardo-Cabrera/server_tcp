import socket

def iniciar_cliente():
    HOST = 'localhost'
    PORT = 5000
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conectado al servidor. Escribe 'DESCONEXION' para salir")
        
        try:
            while True:
                mensaje = input("Ingresar un mensaje: ")

                try:
                    s.sendall(mensaje.encode())
                except BrokenPipeError:
                    print("Error: Conexión cerrada por el servidor")
                    break
                
                if mensaje.upper() == "DESCONEXION":
                    break
                    
                try:
                    data = s.recv(1024)

                    if not data:
                        print("El servidor ha cerrado la conexión")
                        break
                        
                    print(f"Servidor responde: {data.decode()}")
                except ConnectionResetError:
                    print("Conexión reiniciada por el servidor")
                    break
        except KeyboardInterrupt:
            print("\nInterrupción detectada, desconectando...")
        finally:
            print("Desconectado")

if __name__ == "__main__":
    iniciar_cliente()
