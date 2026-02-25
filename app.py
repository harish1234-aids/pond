from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hunt')
def hunt():
    return render_template('game.html') # The mini-game code you shared

if __name__ == '__main__':
    app.run(debug=True)