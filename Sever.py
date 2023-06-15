import socket
import threading

class GameServer:
    def __init__(self):
        self.host = 'localhost'  # Dirección IP del servidor
        self.port = 8000  # Puerto para la conexión
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.clients = []
        self.threads = []

    def start(self):
        self.server.listen(5)
        print("Servidor iniciado. Esperando conexiones...")
        while True:
            client, address = self.server.accept()
            print(f"Nueva conexión establecida: {address}")
            self.clients.append(client)
            thread = threading.Thread(target=self.handle_client, args=(client,))
            self.threads.append(thread)
            thread.start()

    def handle_client(self, client):
        while True:
            try:
                data = client.recv(1024).decode()
                if data == "create_room":
                    room_id = self.create_room()
                    client.sendall(str(room_id).encode())
                elif data == "join_room":
                    room_id = client.recv(1024).decode()
                    self.join_room(client, room_id)
                    break
            except Exception as e:
                print(f"Error al manejar al cliente: {e}")
                break

    def create_room(self):
        # Lógica para crear una nueva sala y devolver su ID
        pass

    def join_room(self, client, room_id):
        # Lógica para unirse a una sala existente
        pass

if __name__ == '__main__':
    game_server = GameServer()
    game_server.start()