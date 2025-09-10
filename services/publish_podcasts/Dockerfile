FROM python:3.10-slim

WORKDIR /app

COPY services/publish_podcasts/requirements.txt .

RUN pip install -r requirements.txt

COPY services/publish_podcasts /app/services/publish_podcasts
COPY utils/configurations /app/utils/configurations
COPY utils/dals /app/utils/dals
COPY utils/logger /app/utils/logger

CMD ["python", "-m" , "services.publish_podcasts.src.main"]