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

# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#########################################################
# DEMOS                                                 #
#########################################################

# Fetches code content from a GitHub repository using the GitHub API
def fetch_code_content(owner, repo, file_path):
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{file_path}'
    headers = {
        'Authorization': f'token {app.config["GITHUB_ACCESS_TOKEN"]}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    content = response.json()['content']
    decoded_content = base64.b64decode(content).decode('utf-8')
    return decoded_content

@app.route('/run-code', methods=['POST'])
def run_code():
    data = request.json
    result = []

    for repo_info in github_repos:
        owner = repo_info['owner']
        name = repo_info['name']

        try:
            code_content = fetch_code_content(owner, name, 'path_to_file_in_repo.py')
            exec_result = {}
            exec(code_content, globals(), exec_result)
            output = exec_result.get('output', 'No output')
        except Exception as e:
            output = str(e)

        result.append({'owner': owner, 'name': name, 'output': output})

    return jsonify(result)

if __name__ == '__main__':
    freezer.freeze()
    app.run(debug=True)
