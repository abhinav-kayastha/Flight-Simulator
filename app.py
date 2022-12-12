from flask import Flask, request
import mysql.connector

def userNameToDB(username):
    sql = f"INSERT INTO username_and_score(username) VALUES ('{username}');"
    cursor = connection.cursor()
    cursor.execute(sql)
    return

#  Database connection
connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="2012004",
    autocommit=True
)

app = Flask(__name__)


@app.route('/user_data', methods=["GET", "POST"])
def user_data():
    if request.method == "POST":
        username = request.form.get("uname")
        userNameToDB(username)
        return "Success"
    else:
        return "Failed"


if __name__ == '__main__':
    app.run()

