FROM python:3.9-slim

WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED=1

CMD ["python", "tip_calculator.py"]
