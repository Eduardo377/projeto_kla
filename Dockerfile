FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Garante que o python está no path correto
ENV PATH="/usr/local/bin:${PATH}"

# Define o entrypoint para garantir a execução correta
ENTRYPOINT ["python3", "auditor_cli.py"]