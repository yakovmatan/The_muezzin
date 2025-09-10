FROM python:3.10-slim

WORKDIR /app

COPY services/text_handling/requirements.txt .

RUN pip install -r requirements.txt

COPY services/text_handling /app/services/text_handling
COPY utils/configurations /app/utils/configurations
COPY utils/dals /app/utils/dals
COPY utils/logger /app/utils/logger

CMD ["python", "-m" , "services.text_handling.src.main"]