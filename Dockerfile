# Usa uma imagem oficial do Python (slim para ser leve)
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do seu PC para o container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para rodar o script
ENTRYPOINT ["python3", "auditor_cli.py"]
