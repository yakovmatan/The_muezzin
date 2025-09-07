FROM python:3.10-slim

WORKDIR /app

COPY processing/requirements.txt .

RUN pip install -r requirements.txt

COPY processing /app/processing
COPY configurations /app/configurations
COPY logger /app/logger

CMD ["python", "-m" , "processing.src.main"]