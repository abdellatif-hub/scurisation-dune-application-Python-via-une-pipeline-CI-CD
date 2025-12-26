FROM python:3.12-slim

WORKDIR /app

# Installer les dépendances en root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Créer utilisateur sécurisé APRÈS installation
RUN useradd appuser
USER appuser

COPY api/ .

EXPOSE 5000
CMD ["python", "app.py"]
