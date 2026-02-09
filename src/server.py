#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor TCP para gerenciamento de vagas de estacionamento.
O servidor escuta conexões de clientes e responde a comandos para consultar,
pegar e liberar vagas.

Autor: ChatGPT e Copilot com orientação e revisão de Minora
Data: 2024-06-15

Procure por FIXME para identificar pontos que precisam de implementação adicional.

"""
import socket
import os
import threading
from dotenv import load_dotenv

# FIXME: Implemente a lógica de gerenciamento de vagas conforme necessário

TOTAL_VAGAS = 10
vagas_disponiveis = TOTAL_VAGAS
leitores = 0

mutex_leitores = threading.Lock()
mutex_escrita = threading.Semaphore(1)

def escutar_cliente(nova_conexao, endereco):
    """Função para tratar a comunicação com cada cliente"""
    print(f'Cliente conectado de {endereco}')
    global vagas_disponiveis, leitores
    try:
        while True:
            mensagem = nova_conexao.recv(1024)
            if not mensagem:
                break            
            comando = mensagem.decode("utf-8").strip()
            print(f'Mensagem recebida de {endereco}: {comando}')
            
            if comando == 'consultar_vaga':
                with mutex_leitores:
                    leitores += 1
                    if leitores == 1:
                        mutex_escrita.acquire()

                resposta = str(vagas_disponiveis)
                nova_conexao.send(resposta.encode('utf-8'))

                with mutex_leitores:
                    leitores -= 1
                    if leitores == 0:
                        mutex_escrita.release()
                
            elif comando == 'pegar_vaga':
                mutex_escrita.acquire()

                if vagas_disponiveis > 0:
                    vagas_disponiveis -= 1
                    resposta = '1'
                else:
                    resposta = '0'

                nova_conexao.send(resposta.encode('utf-8'))
                mutex_escrita.release()
                
            elif comando == 'liberar_vaga':
                mutex_escrita.acquire()

                if vagas_disponiveis < TOTAL_VAGAS:
                    vagas_disponiveis += 1
                    resposta = '1'
                else:
                    resposta = '0'

                nova_conexao.send(resposta.encode('utf-8'))
                mutex_escrita.release()

                
            else:
                # retorna -1 para comando inválido
                resposta = '-1'
                nova_conexao.send(resposta.encode('utf-8'))
                
    finally:
        nova_conexao.close()
        print(f'Cliente {endereco} desconectado')

def iniciar_servidor():
    """Função para iniciar o servidor TCP"""
    load_dotenv()
    PORTA = int(os.getenv('PORT', 5000))

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(('localhost', PORTA))
    servidor.listen(5)
    print(f'Servidor escutando na porta {PORTA}')
    print('Aguardando conexões de clientes...\n')
    return servidor

def main():
    servidor = iniciar_servidor()
    try:
        while True:
            nova_conexao, endereco = servidor.accept()
            thread = threading.Thread(target=escutar_cliente, args=(nova_conexao, endereco))
            thread.daemon = True
            thread.start()
        
    finally:
        servidor.close()
        print('\nServidor encerrado')

if __name__ == '__main__':
    main()
