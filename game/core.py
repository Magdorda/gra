"""

User interface

"""

from flask import Flask, render_template, request
app = Flask(__name__)
import locations

def game():
    pass

@app.route('/', allowed=['GET', 'POST'])
def hello_world():
    word = locations.game_plot(None)
    loc = 'To jest ops lokacji szczegółowy ... w pythonie'
    return render_template('index.html', **{'tomek':'gra', 'location':loc})

if __name__ == "__main__":
    app.run()