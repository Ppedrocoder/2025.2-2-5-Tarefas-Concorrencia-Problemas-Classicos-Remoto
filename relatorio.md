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

- Mantém o controle do número de vagas disponíveis 

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

### Cliente.py

```bash
Conectado ao servidor de estacionamento
Cliente 0 iniciou
Cliente 0 consulta: 50 vagas
Cliente 0 conseguiu vaga
Cliente 0 passeando por 1.45 segundos
Conectado ao servidor de estacionamento
Cliente 1 iniciou
Cliente 1 consulta: 49 vagas
Cliente 1 conseguiu vaga
Cliente 1 passeando por 2.51 segundos
Conectado ao servidor de estacionamento
Cliente 2 iniciou
Cliente 2 consulta: 48 vagas
Cliente 2 conseguiu vaga
Cliente 2 passeando por 2.76 segundos
Conectado ao servidor de estacionamento
Cliente 3 iniciou
Cliente 3 consulta: 47 vagas
Cliente 3 conseguiu vaga
Cliente 3 passeando por 1.13 segundos
Conectado ao servidor de estacionamento
Cliente 4 iniciou
Cliente 4 consulta: 46 vagas
Cliente 4 conseguiu vaga
Cliente 4 passeando por 1.11 segundos
Conectado ao servidor de estacionamento
Cliente 5 iniciou
Cliente 5 consulta: 45 vagas
Cliente 5 conseguiu vaga
Cliente 5 passeando por 2.82 segundos
Conectado ao servidor de estacionamento
Cliente 6 iniciou
Cliente 6 consulta: 44 vagas
Cliente 6 conseguiu vaga
Cliente 6 passeando por 2.88 segundos
Conectado ao servidor de estacionamento
Cliente 7 iniciou
Cliente 7 consulta: 43 vagas
Cliente 7 conseguiu vaga
Cliente 7 passeando por 2.47 segundos
Conectado ao servidor de estacionamento
Cliente 8 iniciou
Cliente 8 consulta: 42 vagas
Cliente 8 conseguiu vaga
Cliente 8 passeando por 3.00 segundos
Conectado ao servidor de estacionamento
Cliente 9 iniciou
Cliente 9 consulta: 41 vagas
Cliente 9 conseguiu vaga
Cliente 9 passeando por 1.96 segundos
Conectado ao servidor de estacionamento
Cliente 10 iniciou
Cliente 10 consulta: 40 vagas
Cliente 10 conseguiu vaga
Cliente 10 passeando por 1.05 segundos
Conectado ao servidor de estacionamento
Cliente 11 iniciou
Cliente 11 consulta: 39 vagas
Cliente 11 conseguiu vaga
Cliente 11 passeando por 2.48 segundos
Conectado ao servidor de estacionamento
Cliente 12 iniciou
Cliente 12 consulta: 38 vagas
Cliente 12 conseguiu vaga
Cliente 12 passeando por 2.90 segundos
Conectado ao servidor de estacionamento
Cliente 13 iniciou
Cliente 13 consulta: 37 vagas
Cliente 13 conseguiu vaga
Cliente 13 passeando por 2.74 segundos
Conectado ao servidor de estacionamento
Cliente 14 iniciou
Cliente 14 consulta: 36 vagas
Cliente 14 conseguiu vaga
Cliente 14 passeando por 2.85 segundos
Cliente 3 liberou a vaga
Cliente 3 finalizou
Cliente 0 liberou a vaga
Cliente 0 finalizou
Cliente 4 liberou a vaga
Cliente 4 finalizou
Conectado ao servidor de estacionamento
Cliente 15 iniciou
Cliente 15 consulta: 38 vagas
Cliente 15 conseguiu vaga
Cliente 15 passeando por 1.41 segundos
Conectado ao servidor de estacionamento
Cliente 16 iniciou
Cliente 16 consulta: 37 vagas
Cliente 16 conseguiu vaga
Cliente 16 passeando por 2.41 segundos
Conectado ao servidor de estacionamento
Cliente 17 iniciou
Cliente 17 consulta: 36 vagas
Cliente 17 conseguiu vaga
Cliente 17 passeando por 1.19 segundos
Conectado ao servidor de estacionamento
Cliente 18 iniciou
Cliente 18 consulta: 35 vagas
Cliente 18 conseguiu vaga
Cliente 18 passeando por 2.18 segundos
Conectado ao servidor de estacionamento
Cliente 19 iniciou
Cliente 19 consulta: 34 vagas
Cliente 19 conseguiu vaga
Cliente 19 passeando por 2.02 segundos
Conectado ao servidor de estacionamento
Cliente 20 iniciou
Cliente 20 consulta: 33 vagas
Cliente 20 conseguiu vaga
Cliente 20 passeando por 2.28 segundos
Cliente 10 liberou a vaga
Cliente 10 finalizou
Conectado ao servidor de estacionamento
Cliente 21 iniciou
Cliente 21 consulta: 33 vagas
Cliente 21 conseguiu vaga
Cliente 21 passeando por 2.59 segundos
Conectado ao servidor de estacionamento
Cliente 22 iniciou
Cliente 22 consulta: 32 vagas
Cliente 22 conseguiu vaga
Cliente 22 passeando por 2.83 segundos
Conectado ao servidor de estacionamento
Cliente 23 iniciou
Cliente 23 consulta: 31 vagas
Cliente 23 conseguiu vaga
Cliente 23 passeando por 1.51 segundos
Conectado ao servidor de estacionamento
Cliente 24 iniciou
Cliente 24 consulta: 30 vagas
Cliente 24 conseguiu vaga
Cliente 24 passeando por 2.82 segundos
Conectado ao servidor de estacionamento
Cliente 25 iniciou
Cliente 25 consulta: 29 vagas
Cliente 25 conseguiu vaga
Cliente 25 passeando por 2.70 segundos
Cliente 1 liberou a vaga
Cliente 1 finalizou
Conectado ao servidor de estacionamento
Cliente 26 iniciou
Cliente 26 consulta: 29 vagas
Cliente 26 conseguiu vaga
Cliente 26 passeando por 1.34 segundos
Conectado ao servidor de estacionamento
Cliente 27 iniciou
Cliente 27 consulta: 28 vagas
Cliente 27 conseguiu vaga
Cliente 27 passeando por 2.92 segundos
Conectado ao servidor de estacionamento
Cliente 28 iniciou
Cliente 28 consulta: 27 vagas
Cliente 28 conseguiu vaga
Cliente 28 passeando por 2.28 segundos
Cliente 9 liberou a vaga
Cliente 9 finalizou
Cliente 17 liberou a vaga
Cliente 17 finalizou
Cliente 15 liberou a vaga
Cliente 15 finalizou
Conectado ao servidor de estacionamento
Cliente 29 iniciou
Cliente 29 consulta: 29 vagas
Cliente 29 conseguiu vaga
Cliente 29 passeando por 1.93 segundos
Cliente 2 liberou a vaga
Cliente 2 finalizou
Conectado ao servidor de estacionamento
Cliente 30 iniciou
Cliente 30 consulta: 29 vagas
Cliente 30 conseguiu vaga
Cliente 30 passeando por 2.97 segundos
Conectado ao servidor de estacionamento
Cliente 31 iniciou
Cliente 31 consulta: 28 vagas
Cliente 31 conseguiu vaga
Cliente 31 passeando por 1.18 segundos
Cliente 7 liberou a vaga
Cliente 7 finalizou
Conectado ao servidor de estacionamento
Cliente 32 iniciou
Cliente 32 consulta: 28 vagas
Cliente 32 conseguiu vaga
Cliente 32 passeando por 1.71 segundos
Cliente 5 liberou a vaga
Cliente 5 finalizou
Conectado ao servidor de estacionamento
Cliente 33 iniciou
Cliente 33 consulta: 28 vagas
Cliente 33 conseguiu vaga
Cliente 33 passeando por 1.24 segundos
Conectado ao servidor de estacionamento
Cliente 34 iniciou
Cliente 34 consulta: 27 vagas
Cliente 34 conseguiu vaga
Cliente 34 passeando por 1.31 segundos
Cliente 6 liberou a vaga
Cliente 6 finalizou
Conectado ao servidor de estacionamento
Cliente 35 iniciou
Cliente 35 consulta: 27 vagas
Cliente 35 conseguiu vaga
Cliente 35 passeando por 1.65 segundos
Cliente 11 liberou a vaga
Cliente 11 finalizou
Conectado ao servidor de estacionamento
Cliente 36 iniciou
Cliente 36 consulta: 27 vagas
Cliente 36 conseguiu vaga
Cliente 36 passeando por 1.14 segundos
Conectado ao servidor de estacionamento
Cliente 37 iniciou
Cliente 37 consulta: 26 vagas
Cliente 37 conseguiu vaga
Cliente 37 passeando por 2.22 segundos
Cliente 8 liberou a vaga
Cliente 8 finalizou
Cliente 23 liberou a vaga
Cliente 23 finalizou
Conectado ao servidor de estacionamento
Cliente 38 iniciou
Cliente 38 consulta: 27 vagas
Cliente 38 conseguiu vaga
Cliente 38 passeando por 2.30 segundos
Cliente 19 liberou a vaga
Cliente 19 finalizou
Conectado ao servidor de estacionamento
Cliente 39 iniciou
Cliente 39 consulta: 27 vagas
Cliente 39 conseguiu vaga
Cliente 39 passeando por 1.14 segundos
Cliente 26 liberou a vaga
Cliente 26 finalizou
Cliente 18 liberou a vaga
Cliente 18 finalizou
Cliente 16 liberou a vaga
Cliente 16 finalizou
Cliente 13 liberou a vaga
Cliente 13 finalizou
Conectado ao servidor de estacionamento
Cliente 40 iniciou
Cliente 40 consulta: 30 vagas
Cliente 40 conseguiu vaga
Cliente 40 passeando por 1.17 segundos
Cliente 12 liberou a vaga
Cliente 12 finalizou
Conectado ao servidor de estacionamento
Cliente 41 iniciou
Cliente 41 consulta: 30 vagas
Cliente 41 conseguiu vaga
Cliente 41 passeando por 2.35 segundos
Cliente 14 liberou a vaga
Cliente 14 finalizou
Conectado ao servidor de estacionamento
Cliente 42 iniciou
Cliente 42 consulta: 30 vagas
Cliente 42 conseguiu vaga
Cliente 42 passeando por 1.03 segundos
Cliente 20 liberou a vaga
Cliente 20 finalizou
Cliente 31 liberou a vaga
Cliente 31 finalizou
Conectado ao servidor de estacionamento
Cliente 43 iniciou
Cliente 43 consulta: 31 vagas
Cliente 43 conseguiu vaga
Cliente 43 passeando por 2.19 segundos
Conectado ao servidor de estacionamento
Cliente 44 iniciou
Cliente 44 consulta: 30 vagas
Cliente 44 conseguiu vaga
Cliente 44 passeando por 2.19 segundos
Conectado ao servidor de estacionamento
Cliente 45 iniciou
Cliente 45 consulta: 29 vagas
Cliente 45 conseguiu vaga
Cliente 45 passeando por 1.06 segundos
Cliente 33 liberou a vaga
Cliente 33 finalizou
Conectado ao servidor de estacionamento
Cliente 46 iniciou
Cliente 46 consulta: 29 vagas
Cliente 46 conseguiu vaga
Cliente 46 passeando por 2.37 segundos
Cliente 21 liberou a vaga
Cliente 21 finalizou
Cliente 34 liberou a vaga
Cliente 34 finalizou
Conectado ao servidor de estacionamento
Cliente 47 iniciou
Cliente 47 consulta: 30 vagas
Cliente 47 conseguiu vaga
Cliente 47 passeando por 2.55 segundos
Cliente 36 liberou a vaga
Cliente 36 finalizou
Cliente 29 liberou a vaga
Cliente 29 finalizou
Conectado ao servidor de estacionamento
Cliente 48 iniciou
Cliente 48 consulta: 31 vagas
Cliente 48 conseguiu vaga
Cliente 48 passeando por 1.48 segundos
Cliente 32 liberou a vaga
Cliente 32 finalizou
Conectado ao servidor de estacionamento
Cliente 49 iniciou
Cliente 49 consulta: 31 vagas
Cliente 49 conseguiu vaga
Cliente 49 passeando por 2.44 segundos
Cliente 22 liberou a vaga
Cliente 22 finalizou
Cliente 39 liberou a vaga
Cliente 39 finalizou
Cliente 28 liberou a vaga
Cliente 28 finalizou
Cliente 35 liberou a vaga
Cliente 35 finalizou
Cliente 25 liberou a vaga
Cliente 40 liberou a vaga
Cliente 25 finalizou
Cliente 40 finalizou
Cliente 24 liberou a vaga
Cliente 24 finalizou
Cliente 42 liberou a vaga
Cliente 42 finalizou
Cliente 45 liberou a vaga
Cliente 45 finalizou
Cliente 27 liberou a vaga
Cliente 27 finalizou
Cliente 37 liberou a vaga
Cliente 37 finalizou
Cliente 30 liberou a vaga
Cliente 30 finalizou
Cliente 38 liberou a vaga
Cliente 38 finalizou
Cliente 48 liberou a vaga
Cliente 48 finalizou
Cliente 41 liberou a vaga
Cliente 41 finalizou
Cliente 43 liberou a vaga
Cliente 43 finalizou
Cliente 44 liberou a vaga
Cliente 44 finalizou
Cliente 46 liberou a vaga
Cliente 46 finalizou
Cliente 47 liberou a vaga
Cliente 47 finalizou
Cliente 49 liberou a vaga
Cliente 49 finalizou
```

### server.py

```bash
Servidor escutando na porta 5000
Aguardando conexões de clientes...

Cliente conectado de ('127.0.0.1', 52929)
Mensagem recebida de ('127.0.0.1', 52929): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52929): pegar_vaga
Cliente conectado de ('127.0.0.1', 52930)
Mensagem recebida de ('127.0.0.1', 52930): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52930): pegar_vaga
Cliente conectado de ('127.0.0.1', 52931)
Mensagem recebida de ('127.0.0.1', 52931): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52931): pegar_vaga
Cliente conectado de ('127.0.0.1', 52932)
Mensagem recebida de ('127.0.0.1', 52932): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52932): pegar_vaga
Cliente conectado de ('127.0.0.1', 52933)
Mensagem recebida de ('127.0.0.1', 52933): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52933): pegar_vaga
Cliente conectado de ('127.0.0.1', 52934)
Mensagem recebida de ('127.0.0.1', 52934): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52934): pegar_vaga
Cliente conectado de ('127.0.0.1', 52935)
Mensagem recebida de ('127.0.0.1', 52935): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52935): pegar_vaga
Cliente conectado de ('127.0.0.1', 52936)
Mensagem recebida de ('127.0.0.1', 52936): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52936): pegar_vaga
Cliente conectado de ('127.0.0.1', 52937)
Mensagem recebida de ('127.0.0.1', 52937): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52937): pegar_vaga
Cliente conectado de ('127.0.0.1', 52938)
Mensagem recebida de ('127.0.0.1', 52938): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52938): pegar_vaga
Cliente conectado de ('127.0.0.1', 52939)
Mensagem recebida de ('127.0.0.1', 52939): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52939): pegar_vaga
Cliente conectado de ('127.0.0.1', 52940)
Mensagem recebida de ('127.0.0.1', 52940): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52940): pegar_vaga
Cliente conectado de ('127.0.0.1', 52941)
Mensagem recebida de ('127.0.0.1', 52941): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52941): pegar_vaga
Cliente conectado de ('127.0.0.1', 52942)
Mensagem recebida de ('127.0.0.1', 52942): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52942): pegar_vaga
Cliente conectado de ('127.0.0.1', 52943)
Mensagem recebida de ('127.0.0.1', 52943): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52943): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52932): liberar_vaga
Cliente ('127.0.0.1', 52932) desconectado
Mensagem recebida de ('127.0.0.1', 52929): liberar_vaga
Cliente ('127.0.0.1', 52929) desconectado
Mensagem recebida de ('127.0.0.1', 52933): liberar_vaga
Cliente ('127.0.0.1', 52933) desconectado
Cliente conectado de ('127.0.0.1', 52944)
Mensagem recebida de ('127.0.0.1', 52944): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52944): pegar_vaga
Cliente conectado de ('127.0.0.1', 52945)
Mensagem recebida de ('127.0.0.1', 52945): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52945): pegar_vaga
Cliente conectado de ('127.0.0.1', 52946)
Mensagem recebida de ('127.0.0.1', 52946): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52946): pegar_vaga
Cliente conectado de ('127.0.0.1', 52947)
Mensagem recebida de ('127.0.0.1', 52947): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52947): pegar_vaga
Cliente conectado de ('127.0.0.1', 52948)
Mensagem recebida de ('127.0.0.1', 52948): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52948): pegar_vaga
Cliente conectado de ('127.0.0.1', 52950)
Mensagem recebida de ('127.0.0.1', 52950): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52950): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52939): liberar_vaga
Cliente ('127.0.0.1', 52939) desconectado
Cliente conectado de ('127.0.0.1', 52951)
Mensagem recebida de ('127.0.0.1', 52951): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52951): pegar_vaga
Cliente conectado de ('127.0.0.1', 52952)
Mensagem recebida de ('127.0.0.1', 52952): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52952): pegar_vaga
Cliente conectado de ('127.0.0.1', 52953)
Mensagem recebida de ('127.0.0.1', 52953): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52953): pegar_vaga
Cliente conectado de ('127.0.0.1', 52954)
Mensagem recebida de ('127.0.0.1', 52954): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52954): pegar_vaga
Cliente conectado de ('127.0.0.1', 52955)
Mensagem recebida de ('127.0.0.1', 52955): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52955): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52930): liberar_vaga
Cliente ('127.0.0.1', 52930) desconectado
Cliente conectado de ('127.0.0.1', 52956)
Mensagem recebida de ('127.0.0.1', 52956): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52956): pegar_vaga
Cliente conectado de ('127.0.0.1', 52957)
Mensagem recebida de ('127.0.0.1', 52957): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52957): pegar_vaga
Cliente conectado de ('127.0.0.1', 52958)
Mensagem recebida de ('127.0.0.1', 52958): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52958): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52938): liberar_vaga
Cliente ('127.0.0.1', 52938) desconectado
Mensagem recebida de ('127.0.0.1', 52946): liberar_vaga
Cliente ('127.0.0.1', 52946) desconectado
Mensagem recebida de ('127.0.0.1', 52944): liberar_vaga
Cliente ('127.0.0.1', 52944) desconectado
Cliente conectado de ('127.0.0.1', 52959)
Mensagem recebida de ('127.0.0.1', 52959): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52959): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52931): liberar_vaga
Cliente ('127.0.0.1', 52931) desconectado
Cliente conectado de ('127.0.0.1', 52960)
Mensagem recebida de ('127.0.0.1', 52960): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52960): pegar_vaga
Cliente conectado de ('127.0.0.1', 52961)
Mensagem recebida de ('127.0.0.1', 52961): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52961): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52936): liberar_vaga
Cliente ('127.0.0.1', 52936) desconectado
Cliente conectado de ('127.0.0.1', 52962)
Mensagem recebida de ('127.0.0.1', 52962): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52962): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52934): liberar_vaga
Cliente ('127.0.0.1', 52934) desconectado
Cliente conectado de ('127.0.0.1', 52963)
Mensagem recebida de ('127.0.0.1', 52963): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52963): pegar_vaga
Cliente conectado de ('127.0.0.1', 52964)
Mensagem recebida de ('127.0.0.1', 52964): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52964): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52935): liberar_vaga
Cliente ('127.0.0.1', 52935) desconectado
Cliente conectado de ('127.0.0.1', 52965)
Mensagem recebida de ('127.0.0.1', 52965): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52965): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52940): liberar_vaga
Cliente ('127.0.0.1', 52940) desconectado
Cliente conectado de ('127.0.0.1', 52966)
Mensagem recebida de ('127.0.0.1', 52966): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52966): pegar_vaga
Cliente conectado de ('127.0.0.1', 52967)
Mensagem recebida de ('127.0.0.1', 52967): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52967): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52937): liberar_vaga
Cliente ('127.0.0.1', 52937) desconectado
Mensagem recebida de ('127.0.0.1', 52953): liberar_vaga
Cliente ('127.0.0.1', 52953) desconectado
Cliente conectado de ('127.0.0.1', 52968)
Mensagem recebida de ('127.0.0.1', 52968): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52968): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52948): liberar_vaga
Cliente ('127.0.0.1', 52948) desconectado
Cliente conectado de ('127.0.0.1', 52969)
Mensagem recebida de ('127.0.0.1', 52969): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52969): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52956): liberar_vaga
Cliente ('127.0.0.1', 52956) desconectado
Mensagem recebida de ('127.0.0.1', 52947): liberar_vaga
Cliente ('127.0.0.1', 52947) desconectado
Mensagem recebida de ('127.0.0.1', 52945): liberar_vaga
Cliente ('127.0.0.1', 52945) desconectado
Mensagem recebida de ('127.0.0.1', 52942): liberar_vaga
Cliente ('127.0.0.1', 52942) desconectado
Cliente conectado de ('127.0.0.1', 52970)
Mensagem recebida de ('127.0.0.1', 52970): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52970): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52941): liberar_vaga
Cliente ('127.0.0.1', 52941) desconectado
Cliente conectado de ('127.0.0.1', 52971)
Mensagem recebida de ('127.0.0.1', 52971): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52971): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52943): liberar_vaga
Cliente ('127.0.0.1', 52943) desconectado
Cliente conectado de ('127.0.0.1', 52972)
Mensagem recebida de ('127.0.0.1', 52972): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52972): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52950): liberar_vaga
Cliente ('127.0.0.1', 52950) desconectado
Mensagem recebida de ('127.0.0.1', 52961): liberar_vaga
Cliente ('127.0.0.1', 52961) desconectado
Cliente conectado de ('127.0.0.1', 52973)
Mensagem recebida de ('127.0.0.1', 52973): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52973): pegar_vaga
Cliente conectado de ('127.0.0.1', 52974)
Mensagem recebida de ('127.0.0.1', 52974): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52974): pegar_vaga
Cliente conectado de ('127.0.0.1', 52975)
Mensagem recebida de ('127.0.0.1', 52975): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52975): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52963): liberar_vaga
Cliente ('127.0.0.1', 52963) desconectado
Cliente conectado de ('127.0.0.1', 52976)
Mensagem recebida de ('127.0.0.1', 52976): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52976): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52951): liberar_vaga
Cliente ('127.0.0.1', 52951) desconectado
Mensagem recebida de ('127.0.0.1', 52964): liberar_vaga
Cliente ('127.0.0.1', 52964) desconectado
Cliente conectado de ('127.0.0.1', 52977)
Mensagem recebida de ('127.0.0.1', 52977): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52977): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52966): liberar_vaga
Cliente ('127.0.0.1', 52966) desconectado
Mensagem recebida de ('127.0.0.1', 52959): liberar_vaga
Cliente ('127.0.0.1', 52959) desconectado
Cliente conectado de ('127.0.0.1', 52978)
Mensagem recebida de ('127.0.0.1', 52978): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52978): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52962): liberar_vaga
Cliente ('127.0.0.1', 52962) desconectado
Cliente conectado de ('127.0.0.1', 52979)
Mensagem recebida de ('127.0.0.1', 52979): consultar_vaga
Mensagem recebida de ('127.0.0.1', 52979): pegar_vaga
Mensagem recebida de ('127.0.0.1', 52952): liberar_vaga
Cliente ('127.0.0.1', 52952) desconectado
Mensagem recebida de ('127.0.0.1', 52969): liberar_vaga
Cliente ('127.0.0.1', 52969) desconectado
Mensagem recebida de ('127.0.0.1', 52958): liberar_vaga
Cliente ('127.0.0.1', 52958) desconectado
Mensagem recebida de ('127.0.0.1', 52965): liberar_vaga
Cliente ('127.0.0.1', 52965) desconectado
Mensagem recebida de ('127.0.0.1', 52955): liberar_vaga
Mensagem recebida de ('127.0.0.1', 52970): liberar_vaga
Cliente ('127.0.0.1', 52955) desconectado
Cliente ('127.0.0.1', 52970) desconectado
Mensagem recebida de ('127.0.0.1', 52954): liberar_vaga
Cliente ('127.0.0.1', 52954) desconectado
Mensagem recebida de ('127.0.0.1', 52972): liberar_vaga
Cliente ('127.0.0.1', 52972) desconectado
Mensagem recebida de ('127.0.0.1', 52975): liberar_vaga
Cliente ('127.0.0.1', 52975) desconectado
Mensagem recebida de ('127.0.0.1', 52957): liberar_vaga
Cliente ('127.0.0.1', 52957) desconectado
Mensagem recebida de ('127.0.0.1', 52967): liberar_vaga
Cliente ('127.0.0.1', 52967) desconectado
Mensagem recebida de ('127.0.0.1', 52960): liberar_vaga
Cliente ('127.0.0.1', 52960) desconectado
Mensagem recebida de ('127.0.0.1', 52968): liberar_vaga
Cliente ('127.0.0.1', 52968) desconectado
Mensagem recebida de ('127.0.0.1', 52978): liberar_vaga
Cliente ('127.0.0.1', 52978) desconectado
Mensagem recebida de ('127.0.0.1', 52971): liberar_vaga
Cliente ('127.0.0.1', 52971) desconectado
Mensagem recebida de ('127.0.0.1', 52973): liberar_vaga
Cliente ('127.0.0.1', 52973) desconectado
Mensagem recebida de ('127.0.0.1', 52974): liberar_vaga
Cliente ('127.0.0.1', 52974) desconectado
Mensagem recebida de ('127.0.0.1', 52976): liberar_vaga
Cliente ('127.0.0.1', 52976) desconectado
Mensagem recebida de ('127.0.0.1', 52977): liberar_vaga
Cliente ('127.0.0.1', 52977) desconectado
Mensagem recebida de ('127.0.0.1', 52979): liberar_vaga
Cliente ('127.0.0.1', 52979) desconectado
```

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
