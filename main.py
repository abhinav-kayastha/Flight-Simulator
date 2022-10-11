#  Importing necessary libraries
from geopy import distance
from random import randint
import mysql.connector


#  Function to get the list of airports in Finland
def getAirports():
    list_of_airports = []
    sql = "SELECT name FROM airport WHERE iso_country = 'FI'" + f";"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for airport in result:
        list_of_airports.append(airport[0])
    return list_of_airports


#  Function to assign certain amount of passengers to each airport
def passengerTravel():
    airport_passenger_amount = {}
    for airport in getAirports():
        airport_passenger_amount[airport] = randint(80, 150)
    return airport_passenger_amount


#  Function to calculate distance between two airports
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


#  Database connection
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

#  Rules/Introduction to the game
print(
    "Welcome to the about page, this page is to help you understand how the game work, how to succeed in the game as well as, the purpose behind this game.\n"
    "In the game you will you will be presented with a list with option to pick you starting airport.\n"
    "Once that has been decided you will be given a list of all the possible airports you can travel to.\n"
    "In addition you also be given a the number of passengers that wish to travel to each airport location, the distance to those airports and the amount of CO2 emitted while travelling to those locations.\n"
    "When you have decided on where you wish to travel write the name of the airport in the console and your location will be updated.\n"
    "The goal of the game is to transport 1000 passenger while using as little CO2 as possible.\n"
    "When the game is over you will be told your 'Fuel efficiency', meaning the average amount of CO2 used to transport a passenger meaning the lower your score, the more efficient you are. This is going to be your score and you can repeat the game as many times as you want if you wish to improve you score.\n"
    "The purpose of the game is teach the player the importance being sustainable.\n"
    "And with all these things in mind, we hope you enjoy our game and learn to be a little bit more sustainable.\n")

#  Getting the username of the player and checking if it is longer than 3 characters
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

#  User input for their starting airport and checking whether it exists
next_location = input("\nEnter your starting airport: ")
while True:
    if next_location in getAirports():
        break
    else:
        print("Enter a valid airport.")
        next_location = input("\nEnter your starting airport: ")

#  constants/variables and removing the player's starting airport
list_of_airports.remove(next_location)
airport_passenger_amount.pop(next_location)
passenger_sum = 0
Fuel_consumed_during_flight = 0
total_distance_travelled = 0
Total_number_passenger = 300
Amount_of_CO2_emitted_per_km = 0.125

#  Logic behind the game
while passenger_sum <= Total_number_passenger:
    if passenger_sum <= Total_number_passenger:
        current_location = next_location
        for airport in list_of_airports:
            print(
                f"{airport}: {airport_passenger_amount[airport]} passengers, Distance to Airport: {round(distanceTravelled(current_location, airport))} km")  # shows airports and how many passengers want to travel there
        print(f"\nTotal amount of passengers transported: {passenger_sum}")
        next_location = input("\nNext Destination: ")
        if next_location in list_of_airports:
            Fuel_consumed_during_flight += round(Amount_of_CO2_emitted_per_km * distanceTravelled(current_location, next_location),
                                                 2)
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
            airport_passenger_amount[airport] = randint(80, 150)  # reassigning passenger amount to each airport
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

print(
    f"Congratulations {screen_name}, you win! You have transported {passenger_sum} passengers, travelled a total distance of {round(total_distance_travelled, 2)} km, by using {Fuel_consumed_during_flight} kg of CO2.\n"
    f"You score is {round((Fuel_consumed_during_flight/passenger_sum), 2)} ")  # win message
