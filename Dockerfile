FROM python:3.9-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

RUN mkdir -p templates
COPY app/templates/index.html templates/

ENV PORT=8080

EXPOSE 8080

CMD ["python", "app.py"]
