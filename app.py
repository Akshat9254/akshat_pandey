from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Name: Akshat Pandey, USN: 1BM20IS015"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
