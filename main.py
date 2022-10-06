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
airport_passenger_amount.pop(starting_location)
passenger_sum = 0

while passenger_sum <= 300:
    if passenger_sum <= 300:
        for airport in list_of_airports:
            print(f"{airport}: {airport_passenger_amount[airport]} passengers")
        print(f"\nTotal amount of passengers transported: {passenger_sum}")
        next_location = input("\nNext Destination: ")
        while True:
            if next_location in list_of_airports:
                passenger_sum += airport_passenger_amount[next_location]
                break
            else:
                next_location = input("\nEnter a valid airport: ")
        for airport in airport_passenger_amount:
            airport_passenger_amount[airport] = randint(80, 150)
        while True:
            if next_location in list_of_airports:
                list_of_airports.remove(next_location)
                airport_passenger_amount.pop(next_location)
                break
            else:
                for airport in airport_passenger_amount:
                    print(f"{airport}: {airport_passenger_amount[airport]} passengers")
                print("\nEnter a valid airport.")
                next_location = input("\nNext Destination: ")

print(f"Congratulations, you win! You have transported {passenger_sum} passengers.")
# co2_budget = 1000
# co2_consumed = 0

