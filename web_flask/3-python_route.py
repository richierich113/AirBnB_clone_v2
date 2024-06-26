#!/usr/bin/python3

'''
Write a script that starts a Flask web application:
    -Your web application must be listening on `0.0.0.0`, port `5000`
    -Routes:
        -`/`: display "Hello HBNB!"
        -`/hbnb`: display "HBNB"
        -`/c/<text>`: display "C " followed by the value of the `text`
        variable (replace underscore `_` symbols with a space ` `)
        -`/python/(<text>)`: display "Python ", followed by the value of
        the `text` variable (replace underscore _ symbols with a space ` `)
            -The default value of text is "is cool"
    -You must use the option `strict_slashes=False` in your route definition
'''


from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'


@app.route('/c/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    text = unquote(text.replace('_', ' '))
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    text = unquote(text.replace('_', ' '))
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
