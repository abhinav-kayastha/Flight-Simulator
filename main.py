import mysql.connector
import random

screen_name = input("Enter Player Name: ")

co2_budget = 1000
co2_consumed = 0

location = "EFHK"


def getAirports():
    sql = "SELECT name FROM airport WHERE iso_country = 'FI'" + f";"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def passengerTravel():
    plane_capacity = 150
    for airport in getAirports():
        airport_passenger = random.randint(0, plane_capacity)
        plane_capacity = plane_capacity - airport_passenger
        airport_passenger = airport + ": " + str(airport_passenger)
    return airport_passenger


connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="2012004",
    autocommit=True
)

print(getAirports())
print(passengerTravel())
