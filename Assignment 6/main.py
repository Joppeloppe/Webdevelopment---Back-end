from flask import Flask, json, jsonify, render_template, redirect, request
import os.path

app = Flask(__name__)


original_book_index = 999

# Index page.
@app.route('/')
def index():
    return render_template('index.html')


# Add new book.
@app.route('/add')
def add_book():
    return render_template('addBook.html')


# Edit a book
@app.route('/edit/<string:title>', defaults={'title': None})
@app.route('/edit/<string:title>', methods=['POST', 'GET'])
def edit(title):
    if os.path.isfile('database.json'):
        if title:
            with open('database.json') as jsonData:
                data = json.load(jsonData)

                book = find_book(data['book'], title)

                for i in range(len(data['book'])):
                    if data['book'][i]['title'] == title:
                        global original_book_index
                        original_book_index = i
                        print(i)

                book_title = book['title']
                book_published = book['published']
                book_author = book['author']

                print(book_title + "\n" + book_published + "\n" + book_author)

    return render_template('editBook.html', title=book_title, published=book_published, author=book_author)


# Success in adding new book.
@app.route('/addnewbook', methods=['POST', 'GET'])
def add_book_page():

    new_book = {
        'title': request.form.get('title', None),
        'published': request.form.get('published', None),
        'author': request.form.get('author', None)
    }

    if add_new_book(new_book) is True:
        return redirect('/add', code=302)
    else:
        return page_not_found(404)


# Success in editing new book.
@app.route('/editbook', methods=['POST', 'GET'])
def edit_book_page():

        book = {
            'title': request.form.get('title', None),
            'published': request.form.get('published', None),
            'author': request.form.get('author', None)
        }

        if edit_book(book) is True:
            return redirect('/', code=302)
        else:
            return page_not_found(404)


# Shows books that are in the library as html.
@app.route('/library/', defaults={'title': None})
@app.route('/library/<string:title>')
def library(title):
    if os.path.isfile('database.json'):
        if title:
            with open('database.json') as jsonData:
                data = json.load(jsonData)

                data = find_book(data['book'], title)

                book = {
                    'book': [data]
                }

                data = book

        elif not title:
            with open('database.json') as jsonData:
                data = json.load(jsonData)
                data = data['book']

        elif title is None:
            with open('database.json') as jsonData:
                data = json.load(jsonData)
                data = data['book']

    return render_template('showLibrary.html', library=data)


# Shows books that are in the library as json objects.
@app.route('/library/api/', defaults={'title': None})
@app.route('/library/api/<string:title>')
def library_json(title):
    if os.path.isfile('database.json'):
        if title:
            with open('database.json') as jsonData:
                data = json.load(jsonData)

                data = find_book(data['book'], title)
                print(data)

        elif not title:
            with open('database.json') as jsonData:
                data = json.load(jsonData)
                print(data)

        elif title is None:
            return page_not_found(404)

        return jsonify(data)

    return render_template('showLibrary.html')

# Error 404.
@app.errorhandler(404)
def page_not_found(error):
    return render_template('pageNotFound.html'), 404


# Checks the library to see if the new book is already in the library or not
def check_library():
    if os.path.isfile('database.json'):
        print('Found file!')
    else:
        json_default = {
            "book": []
        }
        file = open('database.json', 'w')
        json.dump(json_default, file, indent=4, sort_keys=True)
        file.close()

        print('Created a new file!')

    new_title = request.form.get('title', None)

    print('Checking database...')

    with open('database.json', 'r') as jsonData:
        data = json.load(jsonData)
        data_book = data['book']

    found_book = False

    for book in data_book:
        if book['title'] == new_title:
            found_book = True

    return found_book


# Adds a new book from form to json database.
def add_new_book(new_book):
    result = False

    if check_library() is False:

        with open('database.json', 'r') as jsonData:
            data = json.load(jsonData)

        # Add new book to library.
        print('Adding new book to database...')

        data['book'].append(new_book)

        with open('database.json', 'w') as jsonData:
            json.dump(data, jsonData, indent=4, sort_keys=True)

        print('Added new book to the library.')
        result = True

    return result


# Removes a book from the database.
def remove_book(old_book):
    if check_library() is True:

        with open('database.json', 'r') as jsonData:
            data = json.load(jsonData)

        print('Removing book from database...')

        print(original_book_index)
        del data['book'][original_book_index]

        print('Removed book from database...')

        with open('database.json', 'w') as jsonData:
            json.dump(data, jsonData, indent=4, sort_keys=True)


# Edit a book from the json database.
def edit_book(new_book):
    if check_library() is True:

        remove_book(new_book)
        add_new_book(new_book)

        return True


# Searches for a book in the library.
def find_book(json_file, title):
    for search in json_file:
        if search['title'] == title:
            return search

if __name__ == "__main__":
    app.run(debug=True)
