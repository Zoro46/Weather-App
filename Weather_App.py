import requests
import json
import pyttsx3
from prettytable import PrettyTable

def slicing(n):
    return n.split(",")
    

while(True):
    city = input("Enter the name of the city\n")
    ncity = slicing(city)
    Temperature = []
    Wind_Speed = []
    Wind_Direction = []
    Humidity = []
    UV = []
    Visibility_km = []
    Visibility_miles = []
    Last_update = []

    if (city== "q"):
        print("Weather App Closed")
        break

    for i in ncity:
        url = f"https://api.weatherapi.com/v1/current.json?key=eca7b7dce07b40d3a79173345230104&q={i}"

        r = requests.get(url)

        wdic = json.loads(r.text)
        Temp = wdic["current"]["temp_c"]
        wind_speed = wdic["current"]["wind_mph"]
        wind_direc = wdic["current"]["wind_dir"]
        Humi = wdic["current"]["humidity"]
        uv = wdic["current"]["uv"]
        visi_km = wdic["current"]["vis_km"]
        visi_miles = wdic["current"]["vis_miles"]
        Last_upd = wdic["current"]["last_updated"]


        Temperature.append(Temp)
        Wind_Speed.append(wind_speed)
        Wind_Direction.append(wind_direc)
        Humidity.append(Humi)
        UV.append(uv)
        Visibility_km.append(visi_km)
        Visibility_miles.append(visi_miles)
        Last_update.append(Last_upd)

        # print(ncity,Temperature,Wind_Speed,Wind_Direction,Humidity,UV,Visibility_km,Visibility_miles)

    myTable = PrettyTable(["City Name", "Temperature(In C)","Wind_Speed","Wind_Direction","Humidity","UV","Visibility_km","Visibility_miles","Last Update"])

    for n in ncity:
        x = ncity.index(n) 
        print(ncity[x])
        myTable.add_row([f"{ncity[x]}",f"{Temperature[x]}",f"{Wind_Speed[x]}",f"{Wind_Direction[x]}",f"{Humidity[x]}",f"{UV[x]}",f"{Visibility_km[x]}",f"{Visibility_miles[x]}",f"{Last_update[x]}"])
    


    print(myTable)









