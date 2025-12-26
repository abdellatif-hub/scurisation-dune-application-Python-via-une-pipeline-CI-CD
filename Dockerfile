FROM python:3.12-slim

RUN useradd appuser
USER appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api/ .

EXPOSE 5000
CMD ["python", "app.py"]
