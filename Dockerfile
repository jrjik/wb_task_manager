# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "task_manager.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "60"]
