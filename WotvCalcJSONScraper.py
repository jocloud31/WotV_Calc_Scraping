from urllib.request import urlopen
import json

quest_dict = json.loads(urlopen('https://raw.githubusercontent.com/WotVFarmCalculator/wotvfarmcalculator.github.io'
                                '/master/data/QuestsByIName.json').read().decode("utf-8"))
item_dict = json.loads(urlopen('https://raw.githubusercontent.com/WotVFarmCalculator/wotvfarmcalculator.github.io/master/data/en'
                    '/ItemName.json ').read().decode("utf-8"))

print(quest_dict)
print(item_dict)
