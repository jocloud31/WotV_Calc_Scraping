from urllib.request import urlopen
import re


def item_lookup(item_name):
    item_request = item_name
    item_map = urlopen('https://raw.githubusercontent.com/WotVFarmCalculator/wotvfarmcalculator.github.io/master/data/en/ItemName.json ').read().decode("utf-8")
    item_name_index = item_map.find(item_request)
    item_key_index_start = 0
    item_key_index_end = item_name_index - 19
    key_index_counter = item_key_index_end - 1

    while key_index_counter >= 0:
        if item_map[key_index_counter] == "\"":
            item_key_index_start = key_index_counter + 1
            break
        key_index_counter -= 1

    return item_map[item_key_index_start:item_key_index_end]


def find_quests(item_id):
    requested_item = item_id
    quest_list = urlopen('https://raw.githubusercontent.com/WotVFarmCalculator/wotvfarmcalculator.github.io/master/data/QuestsByIName.json ').read().decode("utf-8")
    title_pattern = "\"title\": \""
    requested_item_index = quest_list.find(requested_item)
    index_counter = requested_item_index - 1




item_name = input("What item are you searching for?")
item_id = item_lookup(item_name)
print(item_id)
