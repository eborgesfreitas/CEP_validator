# Validador e Consultor de CEP (ViaCEP API)

---

Este projeto Python demonstra como consultar informações de endereço utilizando a **API pública e gratuita do ViaCEP**. Ele permite que você insira um CEP (com ou sem hífen) e receba de volta detalhes como logradouro, bairro, cidade, estado, UF, DDD e região.

---

## Funcionalidades

* **Validação de CEP:** Verifica se o CEP inserido tem o formato correto (8 dígitos numéricos).
* **Limpeza de Entrada:** Aceita CEPs com ou sem hífen (ex: `12345-678` ou `12345678`).
* **Consulta à API ViaCEP:** Realiza requisições HTTP para a API do ViaCEP.
* **Exibição de Dados:** Apresenta as informações de endereço de forma clara no terminal.
* **Tratamento de Erros:** Lida com falhas de conexão, CEPs não encontrados e respostas inválidas da API.

---

## Como Usar

Siga os passos abaixo para rodar este projeto em sua máquina local:

### 1. Pré-requisitos

Certifique-se de ter o **Python 3** instalado em seu sistema.

### 2. Clonar o Repositório

Primeiro, clone este repositório para o seu ambiente local:

```bash
git clone [https://github.com/eborgesfreitas/CEP_validator.git](https://github.com/eborgesfreitas/CEP_validator.git)
