# 1. Utiliser une image de base officielle Python légère
FROM python:3.10-slim

# 2. Définir le dossier de travail à l'intérieur du conteneur
WORKDIR /app

# 3. Copier le fichier des dépendances dans le conteneur
COPY requirements.txt .

# 4. Installer les dépendances Python requises
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le reste du code (notre fichier app.py) dans le conteneur
COPY app.py .

# 6. Exposer le port 8000 sur lequel l'API va écouter
EXPOSE 8000

# 7. La commande par défaut pour lancer l'application au démarrage du conteneur
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]