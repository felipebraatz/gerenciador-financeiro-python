# Gerenciador de Finanças Pessoais (CLI)

Um programa simples e eficiente de interface de linha de comando (CLI) desenvolvido em Python para auxiliar no controle de finanças pessoais. Este projeto foi criado com o objetivo de demonstrar habilidades em lógica de programação, manipulação de dados em memória e tratamento de erros.

## Funcionalidades

* Adicionar Receitas: Registro de entradas financeiras, com soma automática ao saldo atual.
* Adicionar Despesas: Registro de saídas financeiras, com subtração automática do saldo.
* Listar Movimentações: Exibição de um extrato formatado com todas as operações realizadas, organizadas por ID, categoria, título e valor.
* Visualizar Saldo: Consulta rápida e dinâmica do saldo disponível atualizado.
* Menu Interativo: Sistema de navegação em loop que permite o uso contínuo da ferramenta sem interrupções.

## Pré-requisitos

* Python 3.x instalado no sistema.

## Como executar

1. Faça o clone deste repositório ou faça o download do código-fonte.
2. Abra o terminal (ou prompt de comando).
3. Navegue até o diretório onde o arquivo está localizado.
4. Execute o script com o comando:
   python nome_do_arquivo.py

## Tecnologias e Conceitos Utilizados

O projeto foi construído utilizando os fundamentos da linguagem Python, sem a necessidade de bibliotecas externas:
* Variáveis de escopo global e local.
* Estruturas de repetição (while) para controle de fluxo contínuo.
* Estruturas condicionais (if/elif/else).
* Dicionários aninhados para armazenamento e gestão de dados estruturados.
* Tratamento de exceções (try/except) focado em ValueError, prevenindo falhas caso o usuário insira dados em formatos incorretos.
* Formatação de strings (f-strings) para construção de uma interface textual legível e alinhada.
