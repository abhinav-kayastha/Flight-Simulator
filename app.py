from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/user_data', methods=["GET", "POST"])
def user_data():
    if request.method == "POST":
        username = request.form.get("uname")
        return "Your name is " + username
    else:
        return f"Did not find username."


if __name__ == '__main__':
    app.run()
# hi