FROM python:3.11-slim

WORKDIR /app

COPY services/data_retrieval/requirements.txt .

RUN pip install -r requirements.txt

COPY services/data_retrieval /app/services/data_retrieval
COPY utils/configurations /app/utils/configurations
COPY utils/dals /app/utils/dals
COPY utils/logger /app/utils/logger

EXPOSE 8006

CMD ["uvicorn", "services.data_retrieval.src.main:app", "--host", "0.0.0.0", "--port", "8006"]