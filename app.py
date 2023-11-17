from flask import Flask, render_template, request, jsonify
from flask_frozen import Freezer
import os, config, requests, base64

app = Flask(__name__, 
            static_url_path='',
            static_folder='static',
            template_folder='templates')

app.config['FREEZER_DESTINATION'] = 'docs'
freezer = Freezer(app)
app.config.from_pyfile('config.py')

github_repos = [
    {'owner': 'your_username', 'name': 'python-text-editor'},
    {'owner': 'your_username', 'name': 'other-repo'}
]

github_repo_owner = 'your_username'
github_repo_name = 'python-text-editor'
github_token = os.environ.get('GITHUB_TOKEN') or config.github_token

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# About page
@app.route('/about.html') 
def about():
    return render_template('about.html')

# Resume page
@app.route('/resume.html')  
def resume():
    return render_template('resume.html')

# Projects page
@app.route('/projects.html')  
def projects():
    return render_template('projects.html')

@app.route('/.well-known/discord')
def discord_verification():
    return 'dh=af9549bdfedf8a98fe9430cd7b3030a6553712f6'

# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    freezer.freeze()
    app.run(debug=True)
