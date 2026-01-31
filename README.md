# 🚀 Projeto AWS Flask + Docker + Terraform

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-black?logo=flask)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-24.0-blue?logo=docker)](https://www.docker.com/)
[![Terraform](https://img.shields.io/badge/Terraform-1.6-purple?logo=terraform)](https://www.terraform.io/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws)](https://aws.amazon.com/)

Projeto completo de **API Flask** com **Docker**, infraestrutura provisionada via **Terraform na AWS**, front-end básico em HTML/CSS e teste local com **ngrok**.

---

## 📂 Estrutura do Projeto

meu-projeto/
├── app.py
├── database.py
├── models.py
├── Dockerfile
├── requirements.txt
├── static/
├── templates/
├── terraform/
└── .gitignore


---

## ⚡ Tecnologias

- Python 3 + Flask
- Docker
- Terraform
- AWS EC2 + RDS
- HTML/CSS (Front-end)
- ngrok

---

## 🛠️ Como rodar o projeto

### 1️⃣ Criar ambiente virtual e instalar dependências

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
2️⃣ Rodar Flask localmente
python app.py
API disponível em: http://localhost:5000

3️⃣ Docker
docker build -t minha-api-flask .
docker run -p 5000:5000 minha-api-flask
4️⃣ Terraform (AWS)
cd terraform
terraform init
terraform plan
terraform apply
Provisiona EC2, RDS e rede completa.

5️⃣ Teste com ngrok
ngrok http 5000
Acesse a API via URL pública gerada pelo ngrok.

⚠️ Observações
Arquivos sensíveis como .pem e .env não estão incluídos no repositório.

Projeto pronto para portfólio, currículo ou LinkedIn.

Front-end simples apenas para interação com a API.
