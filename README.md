

#  ALERTA FINANCEIRO 

### Sistema de Monitoramento de Criptomoedas com FastAPI + WebSocket

---

## 🧠 Descrição do Projeto

Este projeto é um **sistema de alertas financeiros em tempo real**, desenvolvido como projeto de estudo para aprofundar conhecimentos em:

* **FastAPI**
* **Programação assíncrona (async/await)**
* **WebSockets**
* **Integração com APIs externas**

O sistema permite que o usuário:

1. Cadastre na base de dados:

   * O **símbolo da criptomoeda** (ex: `BTCUSDT`)
   * Um **valor limite**
2. O sistema consulta automaticamente a **API da Binance** em intervalos regulares.
3. Quando o preço da criptomoeda **fica abaixo do valor limite**, um alerta é gerado.
4. Esse alerta é enviado **instantaneamente via WebSocket** para todos os navegadores conectados.

---

## 🧩 Tecnologias Utilizadas

* **Python 3.12**
* **FastAPI**
* **WebSocket**
* **SQLAlchemy**
* **Alembic**
* **HTTPX**
* **HTML + CSS + JavaScript**
* **API pública da Binance**



## 🔁 Funcionamento do Sistema

1. O servidor inicia um **loop de monitoramento assíncrono**.
2. O loop consulta a API da Binance a cada intervalo configurado.
3. Se o preço do ativo for **menor que o limite cadastrado**, o sistema:

   * Registra o alerta
   * Envia a mensagem para todos os clientes conectados via WebSocket
4. O navegador exibe os alertas em tempo real sem precisar atualizar a página.

---

## 🧪 Exemplo de Alerta

```
⚠️ ALERTA: BTCUSDT caiu para 61780.20 (abaixo do limite de 62000.00)
```

---

## 🚀 Como Executar o Projeto

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Aplicar migrações

```bash
alembic upgrade head
```

### 4️⃣ Iniciar o servidor

```bash
uvicorn main:app --reload
```

### 5️⃣ Abrir o painel Web

Abra no navegador:

```
http://localhost:8000/docs
```
Execute o arquivo index.html

```
ATT: o frontend não é dos melhores😂😂😂(feito por ia)
```
---





