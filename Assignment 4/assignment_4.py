from flask import Flask, render_template

app = Flask(__name__)

# Home page.
@app.route('/')
def index():
	return render_template('index.html')


# Contact me page, with form.
@app.route('/contact')
def contact():
    return render_template('contact.html')


# My favorite movies.
@app.route('/movies')
def movies():
    moviesList = ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"]

    return render_template('movies.html', moviesList=moviesList)


# Welcome page for name.
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)


# Error handling for 404: Page not found.
@app.errorhandler(404)
def page_not_found(error):
    return render_template('pageNotFound.html'), 404


if __name__ == "__main__":
	app.run(debug=True)