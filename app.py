from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello! I am Anshul Vyas</h1><p>This is my portfolio.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
