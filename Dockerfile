# Imagem base do Python
FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da API para dentro do container
COPY app.py .
COPY database.py .
COPY models.py .
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta da API
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]

