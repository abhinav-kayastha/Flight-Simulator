import random
import mysql.connector


def getAirports():
    list_of_airports = []
    sql = "SELECT name FROM airport WHERE iso_country = 'FI'" + f";"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for airport in result:
        list_of_airports.append(airport[0])
    return list_of_airports


def passengerTravel():
    for airport in getAirports():
        print(airport + ": " + str(random.randint(80, 150)))
    return


connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="2012004",
    autocommit=True
)

screen_name = input("Enter Player Name: ")
print("List of airports: " + str(getAirports()))
location = input("Enter your starting airport: ")


# co2_budget = 1000
# co2_consumed = 0

