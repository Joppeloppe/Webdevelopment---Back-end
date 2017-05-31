from flask import Flask, render_template, request, json, jsonify, redirect, url_for
import os.path
app = Flask(__name__)


# Home page.
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/done', methods=['POST', 'GET'])
def done():
    newPerson = {
        'firstname': request.form.get('firstname', None),
        'lastname': request.form.get('lastname', None),
        'personnumber': int(request.form.get('personnumber', None)),
        'email': request.form.get('email', None),
        'adress': request.form.get('adress', None),
        'comment': request.form.get('comment', None)
    }

    with open('database.json', 'r') as jsonData:
        data = json.load(jsonData)

    data["Person"].append(newPerson)

    with open('database.json', 'w') as jsonData:
        json.dump(data, jsonData)

    return render_template('done.html')


@app.route('/users/', defaults={'personnumber': None})
@app.route('/users/<int:personnumber>')
def users(personnumber):
    if os.path.isfile('database.json'):
        if personnumber:
            with open('database.json') as jsonData:
                data = json.load(jsonData)

                data = findPerson(data['Person'], personnumber)
                print(data)

        elif not personnumber:
            with open('database.json') as jsonData:
                data = json.load(jsonData)
                print(data)


        return jsonify(data)
    else:
        return render_template('pageNotFound.html')


# Finding a single person within a json file.
def findPerson(jsonFile, key):
    for search in jsonFile:
        if search['personnumber'] == key:
            return search


# Error handling for 404: Page not found.
@app.errorhandler(404)
def page_not_found(error):
    return render_template('pageNotFound.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
