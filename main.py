import mysql.connector

screen_name = input("Enter Player Name: ")
plane_capacity = 200
co2_budget = 1000
co2_consumed = 0
location = "EFHK"


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='2012004',
    autocommit=True
)


