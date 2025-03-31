FROM python:3.10-slim

WORKDIR /app
COPY apps/bi-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY apps/bi-service/ .
EXPOSE 8005
CMD ["python", "main.py"]
