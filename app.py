from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/game', methods=['GET'])
def game():
    return render_template('01_GamePage.html')


if __name__ == '__main__':
    app.run()
