from flask import Flask

app = Flask(__name__)

CSS = """
<style>
    body {
        background: #0a0f0a;
        color: #c8ffc8;
        font-family: monospace;
        margin: 0;
        padding: 0;
    }
    nav {
        background: #0d150d;
        padding: 1rem 2rem;
        border-bottom: 1px solid #1a3a1a;
    }
    nav a {
        color: #00ff41;
        text-decoration: none;
        margin-right: 2rem;
        font-size: 0.9rem;
    }
    nav a:hover { color: white; }
    .container {
        max-width: 900px;
        margin: 3rem auto;
        padding: 0 2rem;
    }
    h1 {
        color: #00ff41;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    h3 { color: #00cc33; }
    p, li { color: #5a8c5a; line-height: 1.8; }
    ul { padding-left: 1.5rem; }
    .tag {
        display: inline-block;
        background: #00ff4122;
        color: #00ff41;
        border: 1px solid #00ff4155;
        padding: 0.2rem 0.6rem;
        margin: 0.2rem;
        font-size: 0.8rem;
    }
</style>
"""

@app.route('/')
def home():
    return f"""
    {CSS}
    <nav>
        <a href='/'>HOME</a>
        <a href='/about'>ABOUT</a>
        <a href='/projects'>PROJECTS</a>
        <a href='/skills'>SKILLS</a>
        <a href='/contact'>CONTACT</a>
    </nav>
    <div class='container'>
        <h1>ANSHUL VYAS</h1>
        <p>Computer Science Student | Cloud Engineer</p>
        <p>Building real cloud infrastructure on AWS.</p>
    </div>
    """

@app.route('/about')
def about():
    return f"""
    {CSS}
    <nav>
        <a href='/'>HOME</a>
        <a href='/about'>ABOUT</a>
        <a href='/projects'>PROJECTS</a>
        <a href='/skills'>SKILLS</a>
        <a href='/contact'>CONTACT</a>
    </nav>
    <div class='container'>
        <h1>ABOUT ME</h1>
        <p>I am a CS student at JIET Jodhpur (2023-2027).</p>
        <p>I work with AWS, Python, and Linux.</p>
        <p>CGPA: 7.83</p>
    </div>
    """

@app.route('/projects')
def projects():
    return f"""
    {CSS}
    <nav>
        <a href='/'>HOME</a>
        <a href='/about'>ABOUT</a>
        <a href='/projects'>PROJECTS</a>
        <a href='/skills'>SKILLS</a>
        <a href='/contact'>CONTACT</a>
    </nav>
    <div class='container'>
        <h1>PROJECTS</h1>
        <h3>1. Cloud-Based App Deployment (AWS)</h3>
        <p>Deployed Flask app on AWS EC2 with Nginx.</p>
        <span class='tag'>AWS EC2</span>
        <span class='tag'>NGINX</span>
        <span class='tag'>PYTHON</span>
        <h3>2. Insurance Cost Prediction</h3>
        <p>ML model to predict insurance charges using Python.</p>
        <span class='tag'>PYTHON</span>
        <span class='tag'>MACHINE LEARNING</span>
    </div>
    """

@app.route('/skills')
def skills():
    return f"""
    {CSS}
    <nav>
        <a href='/'>HOME</a>
        <a href='/about'>ABOUT</a>
        <a href='/projects'>PROJECTS</a>
        <a href='/skills'>SKILLS</a>
        <a href='/contact'>CONTACT</a>
    </nav>
    <div class='container'>
        <h1>SKILLS</h1>
        <h3>Cloud</h3>
        <span class='tag'>AWS EC2</span>
        <span class='tag'>S3</span>
        <span class='tag'>IAM</span>
        <span class='tag'>RDS</span>
        <h3>Programming</h3>
        <span class='tag'>PYTHON</span>
        <span class='tag'>FLASK</span>
        <h3>Tools</h3>
        <span class='tag'>LINUX</span>
        <span class='tag'>NGINX</span>
        <span class='tag'>GIT</span>
    </div>
    """

@app.route('/contact')
def contact():
    return f"""
    {CSS}
    <nav>
        <a href='/'>HOME</a>
        <a href='/about'>ABOUT</a>
        <a href='/projects'>PROJECTS</a>
        <a href='/skills'>SKILLS</a>
        <a href='/contact'>CONTACT</a>
    </nav>
    <div class='container'>
        <h1>CONTACT</h1>
        <p>Email: vyasanshul318@gmail.com</p>
        <p>Phone: +91-9079286503</p>
        <p>Location: Jodhpur, Rajasthan, India</p>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
