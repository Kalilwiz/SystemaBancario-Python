
# 🏦 Banco Kalil's Data

## 💡 Descrição
Este é um projeto simples de simulação de uma conta bancária feito em Python, executado diretamente no terminal. Ele permite que o usuário realize operações de **depósito**, **saque** e **visualização de extrato**, obedecendo algumas regras de negócio.

---

## 🎯 Funcionalidades

- ✅ **Depósito**
  - Permite depósitos de valores **positivos**.
  - Não aceita valores nulos, negativos ou inválidos.

- ✅ **Saque**
  - Limite de até **3 saques por dia**.
  - Valor máximo por saque de **R$500,00**.
  - Saques só são realizados caso haja **saldo suficiente**.

- ✅ **Extrato**
  - Mostra todo o histórico de operações de **depósito** e **saque**.
  - Exibe também o **saldo atual da conta**.

---

## 📜 Regras de Negócio

- 🚫 Não é permitido:
  - Depósitos de valores negativos.
  - Saques acima de R$500,00 por operação.
  - Mais de 3 saques no mesmo dia.
  - Realizar saque sem saldo suficiente.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado no seu computador.
2. Clone este repositório ou copie o código.
3. Execute no terminal com:

```bash
python banco.py
```

---

## 🖥️ Tecnologias Utilizadas

- 🐍 Python (linguagem principal)
- Terminal / Console

---

## 🎩 Tela de Logout

Ao finalizar, o programa exibe uma mensagem de encerramento divertida com uma carinha feita em ASCII Art:

```
         _____
       /       \
      |  O   O  |
      |    ^    |
      |  \___/  |
       \_______/
```
## 🧑‍💻 Autor

Desenvolvido por **Leonardo Kalil** — Banco Kalil's Data 🏦
