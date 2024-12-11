#Import
import os
import time
import json
import random

#Globals
with open("Paths.json", "r") as f:
    dataPath = json.load(f)

global player_data_path
player_data_path = dataPath["Paths"]["PlayerData"]

global map_data_path
map_data_path = dataPath["Paths"]["MapData"]

global assets_path
assets_path = dataPath["Paths"]["Assets"]

global temp_data_path
temp_path = dataPath["Paths"]["Temp"]

#Functions
def CreatePlayer():
    with open(temp_path, "r") as f:
        dataT = json.load(f)

    os.system("cls")

    loop = 1
    dataT["Temp"]["SkipLoop"] = 0
    dataT["Temp"]["CharacterName"] = " "

    with open(temp_path, "w") as f:
        json.dump(dataT, f, indent=4)

    while loop == 1:
        with open(player_data_path, "r") as f:
            dataP = json.load(f)
        
        print("Please give your Character a Name :D")
        print("------------------------------")
        print("Commands:")
        print("<Character Name> - Create Character!")
        print("/Cancel - Return to the Main Menu!")
        print("")

        global player_name
        player_name = input()

        if player_name == "/Cancel":
            print("Character Creation Proccess has been Canceled!")
            loop = 0
            dataT["Temp"]["SkipLoop"] = 1

            with open(temp_path, "w") as f:
                json.dump(dataT, f, indent=4)

            with open(temp_path, "r") as f:
                dataT = json.load(f)
            
            time.sleep(3)
            os.system("cls")

        elif player_name in dataP["PlayerData"]:
            print("A Character with that Name does already exist!")
            time.sleep(3)
            os.system("cls")
            
        else:
            with open(temp_path, "r") as f:
                dataT = json.load(f)

            dataT["Temp"]["CharacterName"] = f"{player_name}"

            with open(temp_path, "w") as f:
                json.dump(dataT, f, indent=4)

            loop = 0
            os.system("cls")

    if dataT["Temp"]["SkipLoop"] != 1:

        loop = 1
        while loop == 1:
            print("Please give your Character a Class :D")
            print("------------------------------")
            print("Commands:")
            print("/Swordsman - Select the Swordsman Class!")
            print("/Archer - Select the Archer Class!")
            print("/Mage- Select the Mage Class!")
            print("/Cancel - Return to the Main Menu!")
            print("")

            global player_class
            player_class = input()
                
            if player_class == "/Cancel":
                print("Character Creation Proccess has been Canceled!")
                loop = 0
                dataT["Temp"]["SkipLoop"] = 1

                with open(temp_path, "w") as f:
                    json.dump(dataT, f, indent=4)

                with open(temp_path, "r") as f:
                    dataT = json.load(f)

                time.sleep(3)
                os.system("cls")

            elif player_class == "/Swordsman":
                dataP["PlayerData"][f"{player_name}"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Name"] = player_name
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Class"] = "Swordsman"
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Area"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["HP"] = 45
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["MP"] = 20
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["ATK"] = 8
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["DEF"] = 8
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["SPD"] = 4
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Money"] = 100
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Weapon"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Artifact"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Potions"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Potions"]["Potion1"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Potions"]["Potion2"] = 0
                loop = 0
                os.system("cls")

            elif player_class == "/Archer":
                dataP["PlayerData"][f"{player_name}"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Name"] = player_name
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Class"] = "Archer"
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Area"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["HP"] = 35
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["MP"] = 20
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["ATK"] = 6
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["DEF"] = 5
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["SPD"] = 8
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Money"] = 100
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Weapon"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Artifact"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Potions"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Potions"]["Potion1"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Potions"]["Potion2"] = 0
                loop = 0
                os.system("cls")

            elif player_class == "/Mage":
                dataP["PlayerData"][f"{player_name}"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Name"] = player_name
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Class"] = "Mage"
                dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Area"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["HP"] = 30
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["MP"] = 30
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["ATK"] = 8
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["DEF"] = 4
                dataP["PlayerData"][f"{player_name}"]["PlayerStats"]["SPD"] = 6
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Money"] = 100
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Weapon"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Artifact"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Potions"] = {}
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Potions"]["Potion1"] = 0
                dataP["PlayerData"][f"{player_name}"]["PlayerInventory"]["Potions"]["Potion2"] = 0
                loop = 0
                os.system("cls")

            else:
                print("This Command does not Exist!")
                time.sleep(3)
                os.system("cls")
            
        if dataT["Temp"]["SkipLoop"] != 1:
            with open(player_data_path, "w") as f:
                json.dump(dataP, f, indent=4)

            print(f"{player_name} has entered Mistiltale as a {dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Class"]} :D")
            time.sleep(5)
            os.system("cls")

def CreateMap():
    i = 0
    while i < 30:
        i = i + 1

        with open(map_data_path, "r") as f:
            dataM = json.load(f)

        with open(assets_path, "r") as f:
            dataA = json.load(f)

        if i == 1:
            dataM["MapData"][f"{player_name}"] = {}

        dataM["MapData"][f"{player_name}"][f"Area{i}"] = {}

        num = random.randint(1, 100)

        if num >= 1 and num < 31:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["EnvironmentType"] = dataA["Map"]["EnvironmentTypes"]["Plains"]

        elif num >= 31 and num < 51:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["EnvironmentType"] = dataA["Map"]["EnvironmentTypes"]["Forest"]

        elif num >= 51 and num < 71:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["EnvironmentType"] = dataA["Map"]["EnvironmentTypes"]["Snowy Taiga"]

        elif num >= 71 and num < 86:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["EnvironmentType"] = dataA["Map"]["EnvironmentTypes"]["Mountain"]

        elif num >= 86 and num < 96:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["EnvironmentType"] = dataA["Map"]["EnvironmentTypes"]["Desert"]

        else:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["EnvironmentType"] = dataA["Map"]["EnvironmentTypes"]["Sea"]

        num = random.randint(1, 100)

        if num >= 1 and num < 51:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] = dataA["Map"]["AreaTypes"]["Fighting-Area"]

        elif num >= 51 and num < 71:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] = dataA["Map"]["AreaTypes"]["Event-Area"]

        elif num >= 71 and num < 81:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] = dataA["Map"]["AreaTypes"]["Resting-Area"]

        elif num >= 81 and num < 91:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] = dataA["Map"]["AreaTypes"]["Merchant-Area"]

        else:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] = dataA["Map"]["AreaTypes"]["Treasure-Area"]

        with open(map_data_path, "w") as f:
            json.dump(dataM, f, indent=4)

    with open(map_data_path, "r") as f:
        dataM = json.load(f)

    with open(assets_path, "r") as f:
        dataA = json.load(f)


    dataM["MapData"][f"{player_name}"][f"Area10"]["EnvironmentType"] = dataA["Map"]["EnvironmentTypes"]["Cracked Realm"]
    dataM["MapData"][f"{player_name}"][f"Area20"]["EnvironmentType"] = dataA["Map"]["EnvironmentTypes"]["Cracked Realm"]
    dataM["MapData"][f"{player_name}"][f"Area30"]["EnvironmentType"] = dataA["Map"]["EnvironmentTypes"]["Shattered Realm"]

    dataM["MapData"][f"{player_name}"][f"Area9"]["AreaType"] = dataA["Map"]["AreaTypes"]["Resting-Area"]
    dataM["MapData"][f"{player_name}"][f"Area19"]["AreaType"] = dataA["Map"]["AreaTypes"]["Resting-Area"]
    dataM["MapData"][f"{player_name}"][f"Area29"]["AreaType"] = dataA["Map"]["AreaTypes"]["Resting-Area"]

    dataM["MapData"][f"{player_name}"][f"Area10"]["AreaType"] = dataA["Map"]["AreaTypes"]["Miniboss-Area"]
    dataM["MapData"][f"{player_name}"][f"Area20"]["AreaType"] = dataA["Map"]["AreaTypes"]["Miniboss-Area"]

    dataM["MapData"][f"{player_name}"][f"Area30"]["AreaType"] = dataA["Map"]["AreaTypes"]["Boss-Area"]

    with open(map_data_path, "w") as f:
        json.dump(dataM, f, indent=4)

    i = 0
    while i < 30:
        i = i + 1

        with open(map_data_path, "r") as f:
            dataM = json.load(f)

        with open(assets_path, "r") as f:
            dataA = json.load(f)

        if (i == 1 or i == 2 or i == 3 or i == 11 or i == 12 or i == 13 or i == 21 or i == 22 or i == 23 or i == 28) and dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Resting-Area"]:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] = dataA["Map"]["AreaTypes"]["Fighting-Area"]

        if (i == 1 or i == 2 or i == 11 or i == 12 or i == 21 or i == 22) and dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Merchant-Area"]:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] = dataA["Map"]["AreaTypes"]["Fighting-Area"]

        if (i == 1 or i == 2 or i == 11 or i == 12 or i == 21 or i == 22) and dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Treasure-Area"]:
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] = dataA["Map"]["AreaTypes"]["Fighting-Area"]

        with open(map_data_path, "w") as f:
            json.dump(dataM, f, indent=4)
    
    i = 0
    while i < 27:
        i = i + 1

        with open(map_data_path, "r") as f:
            dataM = json.load(f)

        with open(assets_path, "r") as f:
            dataA = json.load(f)

        if dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Resting-Area"] and (dataM["MapData"][f"{player_name}"][f"Area{i+1}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Resting-Area"] or dataM["MapData"][f"{player_name}"][f"Area{i+2}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Resting-Area"] or dataM["MapData"][f"{player_name}"][f"Area{i+3}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Resting-Area"]):
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] = dataA["Map"]["AreaTypes"]["Fighting-Area"]

        if dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Merchant-Area"] and (dataM["MapData"][f"{player_name}"][f"Area{i+1}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Merchant-Area"] or dataM["MapData"][f"{player_name}"][f"Area{i+2}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Merchant-Area"] or dataM["MapData"][f"{player_name}"][f"Area{i+3}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Merchant-Area"]):
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] = dataA["Map"]["AreaTypes"]["Event-Area"]

        if dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Treasure-Area"] and (dataM["MapData"][f"{player_name}"][f"Area{i+1}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Treasure-Area"] or dataM["MapData"][f"{player_name}"][f"Area{i+2}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Treasure-Area"] or dataM["MapData"][f"{player_name}"][f"Area{i+3}"]["AreaType"] == dataA["Map"]["AreaTypes"]["Treasure-Area"]):
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] = dataA["Map"]["AreaTypes"]["Event-Area"]

        with open(map_data_path, "w") as f:
            json.dump(dataM, f, indent=4)

    i = 0
    while i < 30:
        i = i + 1

        with open(map_data_path, "r") as f:
            dataM = json.load(f)

        if dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] == 0:
            with open(map_data_path, "r") as f:
                dataM = json.load(f)
            
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["Enemies"] = {}         
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["Enemies"]["Enemy1"] = 0
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["Enemies"]["Enemy2"] = 0
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["Enemies"]["Enemy3"] = 0
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["Enemies"]["Enemy4"] = 0
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["Enemies"]["Enemy5"] = 0

            with open(map_data_path, "w") as f:
                json.dump(dataM, f, indent=4)

            num = random.randint(1, 100)

            if num >= 1 and num < 41:
                enemy_count = 1

            elif num >= 41 and num < 81:
                enemy_count = 2

            else:
                enemy_count = 3

            x = 0
            while enemy_count > x:
                x = x + 1

                with open(map_data_path, "r") as f:
                    dataM = json.load(f)

                num = random.randint(1, 100)

                if num >= 1 and num < 41:
                    with open(map_data_path, "r") as f:
                        dataM = json.load(f)

                    dataM["MapData"][f"{player_name}"][f"Area{i}"]["Enemies"]["Enemy1"] += 1

                    with open(map_data_path, "w") as f:
                        json.dump(dataM, f, indent=4)

                elif num >= 41 and num < 61:
                    with open(map_data_path, "r") as f:
                        dataM = json.load(f)

                    dataM["MapData"][f"{player_name}"][f"Area{i}"]["Enemies"]["Enemy2"] += 1

                    with open(map_data_path, "w") as f:
                        json.dump(dataM, f, indent=4)

                elif num >= 61 and num < 81:
                    with open(map_data_path, "r") as f:
                        dataM = json.load(f)

                    dataM["MapData"][f"{player_name}"][f"Area{i}"]["Enemies"]["Enemy3"] += 1

                    with open(map_data_path, "w") as f:
                        json.dump(dataM, f, indent=4)

                elif num >= 81 and num < 96:
                    with open(map_data_path, "r") as f:
                        dataM = json.load(f)

                    dataM["MapData"][f"{player_name}"][f"Area{i}"]["Enemies"]["Enemy4"] += 1

                    with open(map_data_path, "w") as f:
                        json.dump(dataM, f, indent=4)

                else:
                    with open(map_data_path, "r") as f:
                        dataM = json.load(f)

                    dataM["MapData"][f"{player_name}"][f"Area{i}"]["Enemies"]["Enemy5"] += 1

                    with open(map_data_path, "w") as f:
                        json.dump(dataM, f, indent=4)

        elif dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] == 1:

            with open(map_data_path, "r") as f:
                dataM = json.load(f)

            dataM["MapData"][f"{player_name}"][f"Area{i}"]["Event"] = {}

            if dataM["MapData"][f"{player_name}"][f"Area{i}"]["EnvironmentType"] == 0:
                num = random.randint(1, 10)
                dataM["MapData"][f"{player_name}"][f"Area{i}"]["Event"] = num

                with open(map_data_path, "w") as f:
                    json.dump(dataM, f, indent=4)

            elif dataM["MapData"][f"{player_name}"][f"Area{i}"]["EnvironmentType"] == 1:
                num = random.randint(1, 8)
                dataM["MapData"][f"{player_name}"][f"Area{i}"]["Event"] = num

                with open(map_data_path, "w") as f:
                    json.dump(dataM, f, indent=4)

            elif dataM["MapData"][f"{player_name}"][f"Area{i}"]["EnvironmentType"] == 2:
                num = random.randint(1, 6)
                dataM["MapData"][f"{player_name}"][f"Area{i}"]["Event"] = num

                with open(map_data_path, "w") as f:
                    json.dump(dataM, f, indent=4)

            elif dataM["MapData"][f"{player_name}"][f"Area{i}"]["EnvironmentType"] == 3:
                num = random.randint(1, 5)
                dataM["MapData"][f"{player_name}"][f"Area{i}"]["Event"] = num

                with open(map_data_path, "w") as f:
                    json.dump(dataM, f, indent=4)

            elif dataM["MapData"][f"{player_name}"][f"Area{i}"]["EnvironmentType"] == 4:
                num = random.randint(1, 5)
                dataM["MapData"][f"{player_name}"][f"Area{i}"]["Event"] = num

                with open(map_data_path, "w") as f:
                    json.dump(dataM, f, indent=4)

            else:
                num = random.randint(1, 3)
                dataM["MapData"][f"{player_name}"][f"Area{i}"]["Event"] = num

                with open(map_data_path, "w") as f:
                    json.dump(dataM, f, indent=4)

        elif dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] == 2:
            with open(map_data_path, "r") as f:
                dataM = json.load(f)

        elif dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] == 3:

            with open(map_data_path, "r") as f:
                dataM = json.load(f)

            dataM["MapData"][f"{player_name}"][f"Area{i}"]["Offers"] = {}

            with open(map_data_path, "w") as f:
                json.dump(dataM, f, indent=4)

            with open(player_data_path, "r") as f:
                dataP = json.load(f)

            if dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Class"] == "Swordsman":

                x = 0
                while x < 2:
                    x = x + 1

                    with open(map_data_path, "r") as f:
                        dataM = json.load(f)

                    num = random.randint(1, 100)

                    if num >= 1 and num < 41:
                        rarity = 0
                    
                    elif num >= 41 and num < 71:
                        rarity = 1

                    elif num >= 71 and num < 86:
                        rarity = 2

                    elif num >= 86 and num < 96:
                        rarity = 3

                    else:
                        rarity = 4

                    if rarity == 0:
                        num = random.randint(1, 7)

                    elif rarity == 1:
                        num = random.randint(8, 11)

                    elif rarity == 2:
                        num = random.randint(12, 15)

                    elif rarity == 3:
                        num = random.randint(16, 18)

                    else:
                        num = random.randint(19, 20)

                    dataM["MapData"][f"{player_name}"][f"Area{i}"]["Offers"][f"Weapon{x}"] = num
                    
                    with open(map_data_path, "w") as f:
                        json.dump(dataM, f, indent=4)

            elif dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Class"] == "Archer":

                x = 0
                while x < 2:
                    x = x + 1

                    with open(map_data_path, "r") as f:
                        dataM = json.load(f)

                    num = random.randint(1, 100)

                    if num >= 1 and num < 41:
                        rarity = 0
                    
                    elif num >= 41 and num < 71:
                        rarity = 1

                    elif num >= 71 and num < 86:
                        rarity = 2

                    elif num >= 86 and num < 96:
                        rarity = 3

                    else:
                        rarity = 4

                    if rarity == 0:
                        num = random.randint(21, 27)

                    elif rarity == 1:
                        num = random.randint(28, 31)

                    elif rarity == 2:
                        num = random.randint(32, 35)

                    elif rarity == 3:
                        num = random.randint(36, 38)

                    else:
                        num = random.randint(39, 40)

                    dataM["MapData"][f"{player_name}"][f"Area{i}"]["Offers"][f"Weapon{x}"] = num
                    
                    with open(map_data_path, "w") as f:
                        json.dump(dataM, f, indent=4)

            elif dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Class"] == "Mage":

                x = 0
                while x < 2:
                    x = x + 1

                    with open(map_data_path, "r") as f:
                        dataM = json.load(f)

                    num = random.randint(1, 100)

                    if num >= 1 and num < 41:
                        rarity = 0
                    
                    elif num >= 41 and num < 71:
                        rarity = 1

                    elif num >= 71 and num < 86:
                        rarity = 2

                    elif num >= 86 and num < 96:
                        rarity = 3

                    else:
                        rarity = 4

                    if rarity == 0:
                        num = random.randint(41, 47)

                    elif rarity == 1:
                        num = random.randint(48, 51)

                    elif rarity == 2:
                        num = random.randint(52, 55)

                    elif rarity == 3:
                        num = random.randint(56, 58)

                    else:
                        num = random.randint(59, 60)

                    dataM["MapData"][f"{player_name}"][f"Area{i}"]["Offers"][f"Weapon{x}"] = num
                    
                    with open(map_data_path, "w") as f:
                        json.dump(dataM, f, indent=4)

            x = 0
            while x < 2:
                x = x + 1

                with open(map_data_path, "r") as f:
                    dataM = json.load(f)

                num = random.randint(1, 100)

                if num >= 1 and num < 41:
                    rarity = 0
                    
                elif num >= 41 and num < 71:
                    rarity = 1

                elif num >= 71 and num < 86:
                    rarity = 2

                elif num >= 86 and num < 96:
                    rarity = 3

                else:
                    rarity = 4

                if rarity == 0:
                    num = random.randint(1, 7)

                elif rarity == 1:
                    num = random.randint(8, 11)

                elif rarity == 2:
                    num = random.randint(12, 15)

                elif rarity == 3:
                    num = random.randint(16, 18)

                else:
                    num = random.randint(19, 20)

                dataM["MapData"][f"{player_name}"][f"Area{i}"]["Offers"][f"Artifact{x}"] = num
                    
                with open(map_data_path, "w") as f:
                    json.dump(dataM, f, indent=4)

            x = 0
            while x < 2:
                x = x + 1

                with open(map_data_path, "r") as f:
                    dataM = json.load(f)

                num = random.randint(1, 10)

                dataM["MapData"][f"{player_name}"][f"Area{i}"]["Offers"][f"Potion{x}"] = num

                with open(map_data_path, "w") as f:
                    json.dump(dataM, f, indent=4)

        elif dataM["MapData"][f"{player_name}"][f"Area{i}"]["AreaType"] == 4:
            with open(map_data_path, "r") as f:
                dataM = json.load(f)

            num = random.randint(0, 2)
            dataM["MapData"][f"{player_name}"][f"Area{i}"]["TreasureType"] = num

            with open(map_data_path, "w") as f:
                json.dump(dataM, f, indent=4)

            with open(map_data_path, "r") as f:
                dataM = json.load(f)

            if dataM["MapData"][f"{player_name}"][f"Area{i}"]["TreasureType"] == 0:

                with open(player_data_path, "r") as f:
                    dataP = json.load(f)

                if dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Class"] == "Swordsman":
                    num = random.randint(1, 100)

                    if num >= 1 and num < 41:
                        rarity = 0
                    
                    elif num >= 41 and num < 71:
                        rarity = 1

                    elif num >= 71 and num < 86:
                        rarity = 2

                    elif num >= 86 and num < 96:
                        rarity = 3

                    else:
                        rarity = 4

                    if rarity == 0:
                        num = random.randint(1, 7)

                    elif rarity == 1:
                        num = random.randint(8, 11)

                    elif rarity == 2:
                        num = random.randint(12, 15)

                    elif rarity == 3:
                        num = random.randint(16, 18)

                    else:
                        num = random.randint(19, 20)

                    dataM["MapData"][f"{player_name}"][f"Area{i}"]["TreasureTypeObject"] = num

                    with open(map_data_path, "w") as f:
                        json.dump(dataM, f, indent=4)

                elif dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Class"] == "Archer":
                    num = random.randint(1, 100)

                    if num >= 1 and num < 41:
                        rarity = 0
                    
                    elif num >= 41 and num < 71:
                        rarity = 1

                    elif num >= 71 and num < 86:
                        rarity = 2

                    elif num >= 86 and num < 96:
                        rarity = 3

                    else:
                        rarity = 4

                    if rarity == 0:
                        num = random.randint(21, 27)

                    elif rarity == 1:
                        num = random.randint(28, 31)

                    elif rarity == 2:
                        num = random.randint(32, 35)

                    elif rarity == 3:
                        num = random.randint(36, 38)

                    else:
                        num = random.randint(39, 40)

                    dataM["MapData"][f"{player_name}"][f"Area{i}"]["TreasureTypeObject"] = num

                    with open(map_data_path, "w") as f:
                        json.dump(dataM, f, indent=4)

                elif dataP["PlayerData"][f"{player_name}"]["PlayerInfo"]["Class"] == "Mage":
                    num = random.randint(1, 100)

                    if num >= 1 and num < 41:
                        rarity = 0
                    
                    elif num >= 41 and num < 71:
                        rarity = 1

                    elif num >= 71 and num < 86:
                        rarity = 2

                    elif num >= 86 and num < 96:
                        rarity = 3

                    else:
                        rarity = 4

                    if rarity == 0:
                        num = random.randint(41, 47)

                    elif rarity == 1:
                        num = random.randint(48, 51)

                    elif rarity == 2:
                        num = random.randint(52, 55)

                    elif rarity == 3:
                        num = random.randint(56, 58)

                    else:
                        num = random.randint(59, 60)

                    dataM["MapData"][f"{player_name}"][f"Area{i}"]["TreasureTypeObject"] = num

                    with open(map_data_path, "w") as f:
                        json.dump(dataM, f, indent=4)

            elif dataM["MapData"][f"{player_name}"][f"Area{i}"]["TreasureType"] == 1:
                num = random.randint(1, 100)

                if num >= 1 and num < 41:
                    rarity = 0
                    
                elif num >= 41 and num < 71:
                    rarity = 1

                elif num >= 71 and num < 86:
                    rarity = 2

                elif num >= 86 and num < 96:
                    rarity = 3

                else:
                    rarity = 4

                if rarity == 0:
                    num = random.randint(1, 7)

                elif rarity == 1:
                    num = random.randint(8, 11)

                elif rarity == 2:
                    num = random.randint(12, 15)

                elif rarity == 3:
                    num = random.randint(16, 18)

                else:
                    num = random.randint(19, 20)

                dataM["MapData"][f"{player_name}"][f"Area{i}"]["TreasureTypeObject"] = num
                    
                with open(map_data_path, "w") as f:
                    json.dump(dataM, f, indent=4)

                with open(map_data_path, "w") as f:
                    json.dump(dataM, f, indent=4)

            else:
                num = random.randint(1, 10)
                dataM["MapData"][f"{player_name}"][f"Area{i}"]["TreasureTypeObject"] = num

                with open(map_data_path, "w") as f:
                    json.dump(dataM, f, indent=4)

def DeletePlayer():
    os.system("cls")

    loop = 1
    while loop == 1:
        with open(player_data_path, "r") as f:
            dataP = json.load(f)

        with open(map_data_path, "r") as f:
            dataM = json.load(f)

        print("Wich Character do you want to Delete?")
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
        print("<Character Name> - Delete Character!")
        print("/Cancel - Return to the Main Menu!")
        print("")

        command = input()

        if command in dataP["PlayerData"]:
            del dataP["PlayerData"][f"{command}"]
            del dataM["MapData"][f"{command}"]

            with open(player_data_path, "w") as f:
                json.dump(dataP, f, indent=4)

            with open(map_data_path, "w") as f:
                json.dump(dataM, f, indent=4)
            
            print(f"{command} has been Deleted!")
            time.sleep(5)
            os.system("cls")

        elif command == "/Cancel":
            print("Character Deletion Proccess has been Canceled!")
            loop = 0
            time.sleep(3)
            os.system("cls")

        else:
            print("This Command does not Exist!")
            time.sleep(3)
            os.system("cls")