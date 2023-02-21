from flask import Flask, request
import pytesseract
import psycopg2

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/michael', methods=['GET'])
def michael():
    return "<p>Michael, melech</p>"

@app.route('/ocr', methods=['POST'])
def ocr_api():
  # Receive the file from the client
  file = request.files['file']

  # Perform OCR on the file
  text = pytesseract.image_to_string(file)

  # Connect to the PostgreSQL database
  conn = psycopg2.connect(host="localhost", user="user", password="password", database="database")
  cursor = conn.cursor()

  # Insert the OCR results into the database
  cursor.execute("INSERT INTO ocr_results (text) VALUES (%s)", (text,))
  conn.commit()
  cursor.close()
  conn.close()

  return "OCR results stored in database"

if __name__ == '__main__':
  app.run(
    host="0.0.0.0",
    port=5000
  )

