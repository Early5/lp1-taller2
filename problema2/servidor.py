#!/usr/bin/env python3
"""
Problema 2: Comunicación bidireccional - Servidor
Objetivo: Crear un servidor TCP que devuelva exactamente lo que recibe del cliente
"""

import socket

HOST = "localhost"
PORT = 9000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()



while True:

    print("El servidor 'Echo' a la espera de conexiones ...")
    
    
    cliente, direccion = servidor.accept()
    print(f"un cliente se conecto desde la direccion {direccion}")

    
    datos = cliente.recv(1024)
    if not datos:
        break

    # Mostrar los datos recibidos (en formato bytes)
    print("Datos recibidos:", datos)
    cliente.sendall(datos)
    
    
    cliente.close()

