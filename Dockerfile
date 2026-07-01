FROM python:3.12-slim

WORKDIR /app
COPY api ./api

EXPOSE 8000
CMD ["python", "api/app.py"]
