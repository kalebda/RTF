FROM python:3.9-slim-buster

RUN apt-get update && apt-get -y install libmagic1 curl unzip

## add WORKDIR to enable reloads, uvcorn cannot reload if started from root 
WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install --default-timeout=10000 uvicorn[standard] gunicorn  alembic

COPY . .

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

RUN chmod +x ./start.sh

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
RUN chown -R appuser:appuser /app
RUN chmod 755 /app
USER appuser


CMD ["./start.sh"]
