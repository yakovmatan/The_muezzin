FROM python:3.10-slim

WORKDIR /app

COPY publish_podcasts/requirements.txt .

RUN pip install -r requirements.txt

COPY publish_podcasts /app/publish_podcasts
COPY configurations /app/configurations
COPY logger /app/logger

CMD ["python", "-m" , "publish_podcasts.src.main"]