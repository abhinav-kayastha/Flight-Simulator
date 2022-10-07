from geopy import distance
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


def distanceTravelled(current_location, future_location):
    coordinate_1 = []
    coordinate_2 = []
    sql1 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE name = '{current_location}'" + f";"
    sql2 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE name = '{future_location}'" + f";"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    result1 = cursor1.fetchall()
    cursor2 = connection.cursor()
    cursor2.execute(sql2)
    result2 = cursor2.fetchall()
    for coordinate in result1:
        coordinate_1.append(coordinate)
    for coordinate in result2:
        coordinate_2.append(coordinate)
    distance_travelled = round(distance.distance(tuple(coordinate_1), tuple(coordinate_2)).km, 3)
    return distance_travelled


connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flightgame",
    user="root",
    password="AabanPrasla",
    autocommit=True
)

list_of_airports = getAirports()
airport_passenger_amount = passengerTravel()
print("Welcome to the about page, this page is to help you understand the purpose behind this game, explain the rules of the game and, most importantly how to win in the game.\n"
      "Firstly starting of with the purpose, the purpose of the game is teach the player the importance being sustainable. Recent years, us humans have taken everything for granted and excepted that our current lifestyle will continue but this is not possible so this game wishes to show how being recyclable is rewarding.\n"
      "Secondly, the rules of the games are...\n"
      "Thirdly, the aim of the game is to transport as many passengers as possible using as little co2 as possible.\n"
      "And with all these things in mind, we hope you enjoy our game and learn to be a little bit more sustainable.\n")
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

next_location = input("\nEnter your starting airport: ")
while True:
    if next_location in getAirports():
        break
    else:
        print("Enter a valid airport.")
        next_location = input("\nEnter your starting airport: ")

list_of_airports.remove(next_location)
airport_passenger_amount.pop(next_location)
passenger_sum = 0
fuel_efficiency = 0
total_distance_travelled = 0
Total_number_passenger = 300
Amount_of_CO2_emitted_per_km = 0.125

while passenger_sum <= Total_number_passenger:
    if passenger_sum <= Total_number_passenger:
        current_location = next_location
        for airport in list_of_airports:
            print(f"{airport}: {airport_passenger_amount[airport]} passengers, Distance to Airport: {round(distanceTravelled(current_location, airport))} km")
        print(f"\nTotal amount of passengers transported: {passenger_sum}")
        next_location = input("\nNext Destination: ")
        if next_location in list_of_airports:
            fuel_efficiency += round(Amount_of_CO2_emitted_per_km * distanceTravelled(current_location, next_location), 2)
            total_distance_travelled += distanceTravelled(current_location, next_location)
        else:
            continue
        while True:
            if next_location in list_of_airports:
                passenger_sum += airport_passenger_amount[next_location]
                current_location = next_location
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
                current_location = next_location

print(f"Congratulations {screen_name}, you win! You have transported {passenger_sum} passengers, travelled a total distance of {round(total_distance_travelled, 2)} km, by using {fuel_efficiency} kg of CO2.")

