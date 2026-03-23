from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hello! I am Anshul Vyas</h1>
    <p>This is my portfolio.</p>
    <a href='/about'>About</a> |
    <a href='/contact'>Contact</a>
    """

@app.route('/about')
def about():
    return """
    <h1>About Me</h1>
    <p>I am a Computer Science student at JIET, Jodhpur.</p>
    <p>I work with AWS, Python, and Linux.</p>
    <a href='/'>Home</a>
    """

@app.route('/contact')
def contact():
    return """
    <h1>Contact</h1>
    <p>Email: vyasanshul318@gmail.com</p>
    <p>Phone: +91-9079286503</p>
    <a href='/'>Home</a>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
