FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install gunicorn

COPY . /app

EXPOSE 8003

CMD ["gunicorn", "--bind", "0.0.0.0:8003", "app.routes:app"]
