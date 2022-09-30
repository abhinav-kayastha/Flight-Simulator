from random import randint
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
    airport_passenger_amount = {}
    for airport in getAirports():
        airport_passenger_amount[airport] = randint(80, 150)
    return airport_passenger_amount


connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="2012004",
    autocommit=True
)

list_of_airports = getAirports()
airport_passenger_amount = passengerTravel()

screen_name = input("Enter Player Name (min. 3 characters): ")
while True:
    if len(screen_name) >= 3:
        break
    else:
        print("Enter a player name with a minimum of 3 characters.")
        screen_name = input("Enter Player Name (min. 3 characters): ")

print("List of airports: \n")
for airport in list_of_airports:
    print(airport)

starting_location = input("\nEnter your starting airport: ")
while True:
    if starting_location in getAirports():
        break
    else:
        print("Enter a valid airport.")
        starting_location = input("\nEnter your starting airport: ")

list_of_airports.remove(starting_location)

while True:
    while True:
        next_location = input("Next Destination: ")
        for airport in list_of_airports:
            print(airport)
        while True:
            if next_location in list_of_airports:
                list_of_airports.remove(next_location)
                break
            else:
                print("\nEnter a valid airport.")
                next_location = input("\nNext Destination: ")

# co2_budget = 1000
# co2_consumed = 0
