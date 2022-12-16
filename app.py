from flask import Flask, render_template
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
    password="yoyo@123",
    autocommit=True
)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('01_GamePage.html')


if __name__ == '__main__':
    app.run()

