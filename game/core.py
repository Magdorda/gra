"""

User interface

"""

from flask import Flask, render_template, request
app = Flask(__name__)

import person

@app.route('/')
def hello_world():
    person = person.Person()
    loc = 'To jest ops lokacji szczegółowy ... w pythonie'
    return render_template('index.html', **{'tomek':'gra', 'location':loc})

if __name__ == "__main__":
    app.run()
    pass