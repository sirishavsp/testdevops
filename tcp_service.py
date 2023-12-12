import socket



def start_tcp_server(ip, port):

  # Create a socket object using TCP/IP protocol

  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



  # Bind the socket to the address and port

  server_socket.bind((ip, port))



  # Listen for incoming connections (max 5 connections)

  server_socket.listen(5)

  print(f"Listening on port {port}...")



  while True:

    # Accept a new connection

    client_socket, addr = server_socket.accept()

    print(f"Accepted connection from {addr}")



    # Respond to the client

    message = "Hello, you've connected to the server!\n"

    client_socket.sendall(message.encode())



    # Close the connection

    client_socket.close()



if __name__ == "__main__":

  # Specify the IP address and port number

  # (use '' for IP to accept connections on all available interfaces)

  IP = ''

  PORT = 8080 # The port number to listen on (non-privileged ports are > 1023)



  start_tcp_server(IP, PORT)


