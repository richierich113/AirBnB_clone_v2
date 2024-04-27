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
        -`/number/<n>`: display "`n` is a number" **only** if `n` is an integer
        -`/number_template/<n>`: display a HTML page **only** if `n` is
        an integer:
            -`H1` tag: "Number: `n`" inside the tag `BODY`
        -`/number_odd_or_even/<n>`: display a HTML page **only** if `n` is an
        integer:
            -`H1` tag: "Number: `n` is `even|odd`" inside the tag `BODY`
    -You must use the option `strict_slashes=False` in your route definition
'''


from flask import Flask, render_template
from urllib.parse import unquote

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    text = unquote(text.replace('_', ' '))
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    text = unquote(text.replace('_', ' '))
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    if isinstance(n, int):
        return f'{n} is a number'
    else:
        return 'Not a valid integer'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    if isinstance(n, int):
        return render_template('number.html', n=n)
    else:
        return 'Not a valid integer'


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    if isinstance(n, int):
        odd_or_even = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', n=n, odd_or_even=odd_or_even)
    else:
        return 'Not a valid integer'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
