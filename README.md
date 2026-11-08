# Loan System

Sistema de linha de comando para gerenciamento de uma biblioteca e de empréstimos de livros, desenvolvido em Python.

## Objetivo

Praticar conceitos de programação em um projeto funcional, incluindo:
- variáveis, tipos de dados e estruturas de controle
- funções e organização do código em módulos
- listas e dicionários
- leitura e gravação de dados em arquivos JSON
- lógica de cadastro, empréstimo e devolução

## Funcionalidades

- Cadastrar e listar livros
- Pesquisar livros por título ou autor
- Registrar empréstimos e consultar empréstimos em aberto
- Registrar devoluções e consultar o histórico de movimentações
- Salvar os dados da biblioteca em arquivos JSON

## Estrutura

```text
.
├── main.py
└── lib/
	├── interface.py
	├── register.py
	└── shows.py
```

Os dados são salvos na raiz do projeto nos arquivos `lib.json`, `loans.json` e `moves.json` ao encerrar o programa pelo menu.

## Como executar

É necessário ter Python 3.10 ou superior instalado. Não há dependências externas.

1. Clone o repositório e acesse a pasta do projeto.
2. Execute o programa:

```bash
python3 main.py
```

## Observação

Este projeto foi criado para estudo e prática de Python.
