# Problema dos Leitores e Escritores aplicado ao Controle de Vagas de Estacionamento

## Contexto inicial do trabalho

Este trabalho foi desenvolvido como parte da disciplina de **Sistemas Operacionais**, no semestre letivo **2025.2**, referente à **5ª atividade avaliativa do bimestre**. A atividade teve como objetivo a implementação prática do problema clássico dos **Leitores e Escritores**, utilizando concorrência por meio de threads e comunicação cliente/servidor via sockets em Python.

O problema dos Leitores e Escritores ilustra situações em que múltiplos processos acessam uma área de memória compartilhada, sendo permitido o acesso simultâneo para leitura, enquanto operações de escrita exigem acesso exclusivo, a fim de evitar inconsistências e condições de corrida.

## Descrevendo a solução em Python para o problema de Leitor / Escritor

A solução proposta modela um **estacionamento com vagas limitadas**, no qual múltiplos clientes acessam um servidor central para consultar, ocupar ou liberar vagas. O número de vagas disponíveis representa o recurso compartilhado do sistema.

As operações foram classificadas da seguinte forma:

- **Leitura**: consulta do número de vagas disponíveis (`consultar_vaga`)

- **Escrita**: ocupação (`pegar_vaga`) e liberação (`liberar_vaga`) de vagas

O servidor é responsável por garantir a integridade do recurso compartilhado, enquanto os clientes simulam acessos concorrentes.

## Implementando o servidor e cliente

O sistema foi dividido em dois processos principais:

### Servidor (`server.py`)

O servidor:

- Mantém o controle do número de vagas disponíveis (inicialmente 10)

- Aceita múltiplas conexões simultâneas
- Cria uma thread para cada cliente conectado
- Implementa mecanismos de sincronização para controlar acesso concorrente

### Cliente (`cliente.py`)

O cliente:

- Cria 50 clientes concorrentes utilizando threads

- Cada cliente se conecta ao servidor via socket
- Executa o fluxo:
  1. Consulta vagas

  1. Tenta ocupar uma vaga
  1. Simula o tempo de uso da vaga
  1. Libera a vaga

## Tratando impasse

### Qual a estratégia de tratamento de impasses

Foi utilizada a estratégia clássica do **problema dos Leitores e Escritores**, permitindo:

- **Múltiplos leitores simultâneos**, desde que não haja escritores ativos

- **Acesso exclusivo para escritores**, garantindo que apenas um processo possa modificar o recurso compartilhado por vez

Essa abordagem previne condições de corrida, inconsistência de dados e impasses durante a execução concorrente.

### Implementação do tratamento de impasse em Python

A sincronização foi realizada utilizando:

- `Lock` para controlar o contador de leitores

- `Semaphore` para garantir exclusão mútua nas operações de escrita

Dessa forma, quando o primeiro leitor acessa o recurso, a escrita é bloqueada. Quando o último leitor finaliza, a escrita é liberada novamente.

As operações de escrita (`pegar_vaga` e `liberar_vaga`) utilizam exclusão mútua total, impedindo acessos simultâneos.

## Executar o código e descrever comportamento observado

Durante a execução do sistema, observou-se que:

- Vários clientes conseguem consultar o número de vagas simultaneamente

- Operações de escrita ocorrem de forma exclusiva
- O número de vagas nunca assume valores negativos ou inconsistentes
- Quando todas as vagas são ocupadas, novas consultas retornam zero vagas disponíveis
- O estado do servidor permanece consistente mesmo com múltiplos acessos concorrentes

Os logs exibidos no terminal evidenciam a correta sincronização entre leitores e escritores.

## Considerações finais

A atividade permitiu aplicar na prática conceitos fundamentais de **concorrência**, **sincronização**, **exclusão mútua** e **comunicação entre processos**. A implementação do problema dos Leitores e Escritores mostrou-se eficaz para o controle de acesso a recursos compartilhados em um ambiente concorrente.

O uso adequado de locks e semáforos garantiu a integridade do sistema, evitando condições de corrida e assegurando um comportamento correto mesmo sob alta concorrência, atendendo a todos os requisitos propostos na atividade.

## Conceitos de Concorrência Demonstrados

- Exclusão Mútua: uso de semáforos para escrita

- Sincronização: controle de acesso concorrente ao recurso compartilhado
- Leitores e Escritores: leitura simultânea e escrita exclusiva
- Condição de Corrida: evitada com mecanismos de sincronização
- Programação Concorrente: uso de threads no servidor e nos clientes
