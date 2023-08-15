from flask import Flask, render_template

app = Flask(__name__, 
            static_url_path='',
            static_folder='static',
            template_folder='templates')

#home page
@app.route('/')
def index():
    return render_template('index.html')

#about page
@app.route('/about')
def about():
    return render_template('about.html')

#resume page
@app.route('/resume')
def resume():
    return render_template('resume.html')

#404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)