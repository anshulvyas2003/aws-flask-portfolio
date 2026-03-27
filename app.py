from flask import Flask

app = Flask(__name__)

CSS = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        background: #0a0f0a;
        color: #c8ffc8;
        font-family: monospace;
        animation: fadeIn 0.8s ease;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    nav {
        background: #0d150d;
        padding: 1rem 2rem;
        border-bottom: 1px solid #1a3a1a;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: sticky;
        top: 0;
    }
    .logo {
        color: #00ff41;
        font-size: 1.1rem;
        letter-spacing: 2px;
        text-decoration: none;
    }
    .nav-links a {
        color: #5a8c5a;
        text-decoration: none;
        margin-left: 2rem;
        font-size: 0.85rem;
        letter-spacing: 1px;
        transition: color 0.2s;
    }
    .nav-links a:hover { color: #00ff41; }
    .container {
        max-width: 900px;
        margin: 4rem auto;
        padding: 0 2rem;
    }
    h1 {
        color: #00ff41;
        font-size: 3rem;
        letter-spacing: 3px;
        margin-bottom: 1rem;
        animation: slideIn 0.8s ease;
    }
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    h3 {
        color: #00cc33;
        margin: 1.5rem 0 0.5rem;
        letter-spacing: 2px;
    }
    p, li {
        color: #5a8c5a;
        line-height: 1.8;
        margin-bottom: 0.5rem;
    }
    ul { padding-left: 1.5rem; }
    .tag {
        display: inline-block;
        background: #00ff4122;
        color: #00ff41;
        border: 1px solid #00ff4155;
        padding: 0.2rem 0.8rem;
        margin: 0.2rem;
        font-size: 0.8rem;
        letter-spacing: 1px;
    }
    .card {
        background: #0d150d;
        border: 1px solid #1a3a1a;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: border-color 0.2s, transform 0.2s;
    }
    .card:hover {
        border-color: #00ff41;
        transform: translateX(5px);
    }
    .btn {
        display: inline-block;
        background: #00ff41;
        color: #0a0f0a;
        padding: 0.8rem 2rem;
        text-decoration: none;
        font-family: monospace;
        letter-spacing: 2px;
        margin-top: 1.5rem;
        margin-right: 1rem;
        transition: background 0.2s;
    }
    .btn:hover { background: white; }
    .btn-outline {
        background: transparent;
        color: #00ff41;
        border: 1px solid #00ff41;
    }
    .btn-outline:hover { background: #00ff4122; }
    .divider {
        border: none;
        border-top: 1px solid #1a3a1a;
        margin: 2rem 0;
    }
    footer {
        text-align: center;
        padding: 2rem;
        border-top: 1px solid #1a3a1a;
        color: #1a3a1a;
        font-size: 0.8rem;
        margin-top: 4rem;
    }
    footer span { color: #00ff41; }
</style>
"""

NAV = """
<nav>
    <a href='/' class='logo'>AV://ANSHUL_VYAS</a>
    <div class='nav-links'>
        <a href='/'>HOME</a>
        <a href='/about'>ABOUT</a>
        <a href='/projects'>PROJECTS</a>
        <a href='/skills'>SKILLS</a>
        <a href='/contact'>CONTACT</a>
    </div>
</nav>
"""

FOOTER = """
<footer>
    <span>ANSHUL VYAS</span> — Deployed on AWS EC2 · Mumbai · ap-south-1
</footer>
"""

@app.route('/')
def home():
    return f"""
    {CSS}{NAV}
    <div class='container'>
        <p style='color:#00ff41; letter-spacing:3px; font-size:0.85rem;'>
            // CLOUD ENGINEER & CS STUDENT
        </p>
        <h1>ANSHUL<br>VYAS</h1>
        <p>Computer Science undergraduate building real cloud infrastructure on AWS.</p>
        <p>Passionate about EC2, Linux systems, Python automation, and data analysis.</p>
        <hr class='divider'>
        <a href='/projects' class='btn'>VIEW PROJECTS</a>
        <a href='/contact' class='btn btn-outline'>CONTACT ME</a>
    </div>
    {FOOTER}
    """

@app.route('/about')
def about():
    return f"""
    {CSS}{NAV}
    <div class='container'>
        <h1>ABOUT</h1>
        <div class='card'>
            <h3>EDUCATION</h3>
            <p>B.Tech Computer Science — JIET Jodhpur (2023–2027)</p>
            <p>CGPA: 7.83</p>
        </div>
        <div class='card'>
            <h3>EXPERIENCE</h3>
            <p>Data Analytics Intern — Cleaned datasets, generated reports using Python</p>
            <p>Smart India Hackathon — 2nd Runner Up</p>
            <p>E-Commerce Founder — Built and managed Shopify store</p>
        </div>
        <div class='card'>
            <h3>CERTIFICATIONS</h3>
            <p>✓ Data Analytics in Python</p>
            <p>✓ Python Programming</p>
        </div>
    </div>
    {FOOTER}
    """

@app.route('/projects')
def projects():
    return f"""
    {CSS}{NAV}
    <div class='container'>
        <h1>PROJECTS</h1>
        <div class='card'>
        <div class='card'>
            <p>Performed EDA and feature selection to identify cost-influencing factors.
            Built ML model to predict insurance charges with high accuracy.</p>
            <br>
            <span class='tag'>PYTHON</span>
            <span class='tag'>PANDAS</span>
            <span class='tag'>EDA</span>
    </div>
    {FOOTER}
    """

def skills():
    return f"""
    {CSS}{NAV}
    <div class='container'>
        <h1>SKILLS</h1>
        <div class='card'>
            <span class='tag'>AWS EC2</span>
            <span class='tag'>S3</span>
            <span class='tag'>IAM</span>
            <span class='tag'>RDS</span>
            <span class='tag'>ELASTIC IP</span>
            <span class='tag'>SECURITY GROUPS</span>
        </div>
        <div class='card'>
            <h3>🐍 PROGRAMMING</h3>
            <span class='tag'>PYTHON</span>
            <span class='tag'>FLASK</span>
            <span class='tag'>PANDAS</span>
            <span class='tag'>NUMPY</span>
        </div>
        <div class='card'>
            <h3>🐧 TOOLS</h3>
            <span class='tag'>LINUX</span>
            <span class='tag'>NGINX</span>
            <span class='tag'>GIT</span>
            <span class='tag'>GITHUB</span>
            <span class='tag'>SSH</span>
        </div>
        <div class='card'>
            <h3>📊 DATA</h3>
            <span class='tag'>DATA CLEANING</span>
            <span class='tag'>EDA</span>
            <span class='tag'>VISUALIZATION</span>
            <span class='tag'>ML MODELS</span>
        </div>
    </div>
    {FOOTER}
    """

@app.route('/contact')
def contact():
    return f"""
    {CSS}{NAV}
    <div class='container'>
        <h1>CONTACT</h1>
        <div class='card'>
            <h3>📧 EMAIL</h3>
            <p>vyasanshul318@gmail.com</p>
        </div>
        <div class='card'>
            <h3>📱 PHONE</h3>
            <p>+91-9079286503</p>
        </div>
        <div class='card'>
            <h3>📍 LOCATION</h3>
            <p>Jodhpur, Rajasthan, India 🇮🇳</p>
        </div>
    </div>
    {FOOTER}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
