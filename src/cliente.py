#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cliente TCP para gerenciamento de vagas de estacionamento.
O cliente envia comandos ao servidor para consultar,
pegar e liberar vagas.

Autor: ChatGPT e Copilot com orientação e revisão de Minora
Data: 2024-06-15

Procure por FIXME para identificar pontos que precisam de implementação adicional.

"""

import random
import threading
import socket
import os
import time
from dotenv import load_dotenv


class ClienteEstacionamento(threading.Thread):
    def __init__(self, socket_cliente, id_cliente=None):
        threading.Thread.__init__(self)
        self.socket_cliente = socket_cliente
        self.id_cliente = id_cliente

    def run(self):
        """
        Fluxo do cliente:
        1. Consulta se há vaga
        2. Se houver, tenta pegar a vaga
        3. Passeia (ocupa a vaga por um tempo)
        4. Libera a vaga
        """
        print(f"Cliente {self.id_cliente} iniciou")

        if self.consultar_vaga():
            if self.pegar_vaga():
                self.passear()
                self.liberar_vaga()

        self.socket_cliente.close()
        print(f"Cliente {self.id_cliente} finalizou")

    def consultar_vaga(self):
        try:
            self.socket_cliente.send("consultar_vaga".encode())
            resposta = self.socket_cliente.recv(1024).decode()
            vagas = int(resposta)
            print(f"Cliente {self.id_cliente} consulta: {vagas} vagas")
            return vagas > 0
        except (ConnectionAbortedError, ValueError):
            return False

    def pegar_vaga(self):
        try:
            self.socket_cliente.send("pegar_vaga".encode())
            resposta = self.socket_cliente.recv(1024).decode()
            sucesso = int(resposta)

            if sucesso == 1:
                print(f"Cliente {self.id_cliente} conseguiu vaga")
                self.tem_vaga = True
                return True
            else:
                print(f"Cliente {self.id_cliente} não conseguiu vaga")
                return False

        except ConnectionAbortedError:
            print(f"Cliente {self.id_cliente}: conexão encerrada pelo servidor")
            return False

    def liberar_vaga(self):
        if not self.tem_vaga:
            return False

        try:
            self.socket_cliente.send("liberar_vaga".encode())
            resposta = self.socket_cliente.recv(1024).decode()
            sucesso = int(resposta)

            if sucesso == 1:
                print(f"Cliente {self.id_cliente} liberou a vaga")
            self.tem_vaga = False
            return True

        except ConnectionAbortedError:
            return False

    
    def passear(self):
        tempo = random.uniform(1, 3)
        print(f"Cliente {self.id_cliente} passeando por {tempo:.2f} segundos")
        time.sleep(tempo)

def criar_socket_cliente():
    # Cria e retorna um socket TCP para o cliente.
    load_dotenv()
    PORTA = int(os.getenv('PORT', 5000))

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', PORTA))
    print('Conectado ao servidor de estacionamento')
    return cliente

def main():
    threads = []

    for i in range(10):
        socket_cliente = criar_socket_cliente()
        cliente = ClienteEstacionamento(socket_cliente, id_cliente=i)
        cliente.start()
        threads.append(cliente)
        time.sleep(0.1)  # pequeno atraso para não explodir o servidor 😅

    for t in threads:
        t.join()
if __name__ == "__main__":
    main()