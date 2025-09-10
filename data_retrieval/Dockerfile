FROM python:3.11-slim

WORKDIR /app

COPY data_retrieval/requirements.txt .

RUN pip install -r requirements.txt

COPY data_retrieval /app/data_retrieval
COPY configurations /app/configurations
COPY dals /app/dals
COPY logger /app/logger

EXPOSE 8006

CMD ["uvicorn", "data_retrieval.src.main:app", "--host", "0.0.0.0", "--port", "8006"]