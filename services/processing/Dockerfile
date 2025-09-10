FROM python:3.10-slim

WORKDIR /app

COPY services/processing/requirements.txt .

RUN pip install -r requirements.txt

COPY services/processing /app/services/processing
COPY utils/configurations /app/utils/configurations
COPY utils/dals /app/utils/dals
COPY utils/logger /app/utils/logger

CMD ["python", "-m" , "services.processing.src.main"]