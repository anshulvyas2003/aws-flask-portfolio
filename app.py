from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hello! I am Anshul Vyas</h1>
    <p>Computer Science Student | Cloud Engineer</p>
    <a href='/about'>About</a> |
    <a href='/projects'>Projects</a> |
    <a href='/skills'>Skills</a> |
    <a href='/contact'>Contact</a>
    """

@app.route('/about')
def about():
    return """
    <h1>About Me</h1>
    <p>I am a CS student at JIET Jodhpur (2023-2027).</p>
    <p>I work with AWS, Python, and Linux.</p>
    <a href='/'>Home</a>
    """

@app.route('/projects')
def projects():
    return """
    <h1>My Projects</h1>
    <h3>1. Cloud-Based App Deployment (AWS)</h3>
    <p>Deployed Flask app on AWS EC2 with Nginx.</p>
    <h3>2. Insurance Cost Prediction</h3>
    <p>ML model to predict insurance charges using Python.</p>
    <a href='/'>Home</a>
    """

@app.route('/skills')
def skills():
    return """
    <h1>My Skills</h1>
    <ul>
        <li>AWS (EC2, S3, IAM, RDS)</li>
        <li>Python & Flask</li>
        <li>Linux & Nginx</li>
        <li>Git & GitHub</li>
        <li>Data Analysis & ML</li>
    </ul>
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
