FROM python:3.8

RUN pip install flask psycopg2 pytesseract

COPY . /app
WORKDIR /app

EXPOSE 5000

CMD ["python", "app.py"]
