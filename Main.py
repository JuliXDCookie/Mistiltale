#Import
import os
import time
import json

#Import Assets
from PythonAssets.Functions import CreatePlayer, DeletePlayer, CreateMap

#StartUp
os.system("title Mistiltale")

#Globals
with open("Paths.json", "r") as f:
    dataPath = json.load(f)

global player_data_path
player_data_path = dataPath["Paths"]["PlayerData"]

global map_data_path
map_data_path = dataPath["Paths"]["MapData"]

global temp_data_path
temp_path = dataPath["Paths"]["Temp"]

#Menu
loop = 1
while loop == 1:
    with open(temp_path, "r") as f:
        dataT = json.load(f)

    dataT["Temp"]["SkipLoop"] = 0
    dataT["Temp"]["CharacterName"] = " "

    with open(temp_path, "w") as f:
        json.dump(dataT, f, indent=4)

    with open(player_data_path, "r") as f:
        dataP = json.load(f)
    
    print("Welcome to Mistiltale :D")
    print("------------------------------")
    print("Characters:")
    if dataP["PlayerData"] == {}:
        print("You dont have any Characters :(")

    else:
        for x in dataP["PlayerData"]:
            if dataP["PlayerData"][f"{x}"]["PlayerInfo"]["Area"] == 0:
                area = "Starting Area"

            else:
                area = f"Area {dataP["PlayerData"][f"{x}"]["PlayerInfo"]["Area"]}"
            
            print("<<" + " " + x + " " + "|" + " " + f"{dataP["PlayerData"][f"{x}"]["PlayerInfo"]["Class"]}" + " " + "|" + " " + f"{area}" + " " + ">>")

    print("------------------------------")
    print("Commands:")
    print("/Create - Create a New Character!")
    print("/Delete - Delete a Character!")
    print("")

    command = input()

    if command == "/Create":
        CreatePlayer()

        with open(temp_path, "r") as f:
            dataT = json.load(f)

        if dataT["Temp"]["SkipLoop"] != 1:
            print(f"Generating Map for {dataT["Temp"]["CharacterName"]} :D")
            CreateMap()
        
        os.system("cls")
    
    elif command == "/Delete":
        DeletePlayer()
        os.system("cls")
         
    else:
        print("This Command does not Exist!")
        time.sleep(3)
        os.system("cls")