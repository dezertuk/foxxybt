'''
dict = {'Name':'John', 'Favourite Colour': 'Blue', 'Age':'10'}
print(dict)

dict['Food'] = 'Chicken'

print(dict)


Player
    Name = Jim
    Role = Archer
    HP = 10
    Inventory = Bow, 10 arrow, outfit
        Bow
            DMG = 1
            Value = 3

        Arrow
            DMG = 1
            Value = 2

        Outfit
            Armor = 5
            Value = 12
'''
import json
import datetime

key = str(datetime.datetime.now())
insert = 'Foxxy has turned ON'
logged = {key : insert}

data = json.load(open('StartLog.json', 'r'))
with open('StartLog.json', 'w') as f:
    data['Logs'].update(logged)
    json.dump(data, f, indent=2)

