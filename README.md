# StarkBank Invoice Challenge

Esta aplicação realiza integração com a **Sandbox do Stark Bank** para:
- Emitir de 8 a 12 invoices a cada 3 horas durante 24 horas para pessoas aleatórias.
- Receber callbacks via **webhook** ao pagamento das invoices.
- Efetuar automaticamente uma **transferência do valor recebido (menos eventuais taxas)** para a conta do Stark Bank S.A.

---

## ✅ Propósito

Atender ao desafio técnico da Stark Bank com uma integração simples, funcional e autônoma utilizando **Python** e **Flask**.

---

## ✅ Requisitos

### 📄 Funcionalidades esperadas (em formato BDD)

```gherkin
Feature: Invoice Automation and Webhook Handling

  Scenario: Emitir invoices a cada 3 horas
    Given o sistema está em execução
    When se passam 3 horas
    Then entre 8 e 12 invoices devem ser emitidas para pessoas aleatórias

  Scenario: Processar callback de invoice paga
    Given uma invoice é paga na sandbox do Stark Bank
    When o webhook é chamado com os dados do evento
    Then o sistema deve identificar o valor pago
    And realizar uma transferência para a conta da Stark Bank S.A.
```

---

## 🔧 Requisitos do Sistema

- Python 3.9+
- Conta Sandbox na Stark Bank (com Project e Webhook criados)
- Chave privada `.pem`
- Conta gratuita no [ngrok](https://ngrok.com)

---

## 🚀 Instalação

```bash
# Clone o projeto
git clone https://github.com/marcoscesarmelo/starkbank-invoice-challenge.git
cd starkbank-invoice-challenge

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

---

## ⚙️ Configuração

Crie um arquivo `.env` com:

```env
STARKBANK_PROJECT_ID=seu_project_id
STARKBANK_PRIVATE_KEY_PATH=./private-key.pem
WEBHOOK_URL=https://seu-endereco-ngrok/webhook/invoice
```

E salve sua chave `.pem` no mesmo diretório.

---

## 🔄 Execução

### 1. Inicie o webhook local

```bash
python webhook.py
```

### 2. Inicie o túnel com o ngrok

```bash
ngrok http 5000
```

Copie a URL HTTPS gerada e atualize `WEBHOOK_URL` no `.env`.

### 3. Registre o webhook manualmente (se necessário)

Acesse a [página de Webhooks da Stark Bank](https://starkbank.com/br/sandbox) e insira a URL `https://xxxx.ngrok-free.app/webhook/invoice`.

### 4. Inicie o envio de invoices

```bash
python invoices.py
```

---

## 🧪 Teste

Você pode acompanhar o log de execução dos scripts no terminal e também via interface do ngrok (`http://127.0.0.1:4040`) para ver os POSTs recebidos.

---

## 📤 Transferência automática

Toda vez que uma invoice for paga, será criada uma **transferência automática** para:

- **Banco:** 20018183  
- **Agência:** 0001  
- **Conta:** 6341320293482496  
- **Nome:** Stark Bank S.A.  
- **CNPJ:** 20.018.183/0001-80  
- **Tipo de conta:** payment  

---
