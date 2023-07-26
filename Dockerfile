FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt main.py handlers.py db.json validators.py test_app.py /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["bash", "-c", "pytest && python main.py"]
