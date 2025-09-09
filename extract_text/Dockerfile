FROM python:3.10-slim

WORKDIR /app

COPY extract_text/requirements.txt .

RUN pip install -r requirements.txt

COPY extract_text /app/extract_text
COPY configurations /app/configurations
COPY dals /app/dals
COPY logger /app/logger

CMD ["python", "-m" , "extract_text.src.main"]