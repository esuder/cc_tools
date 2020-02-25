import cc_dat_utils
import cc_classes
import json

#Part 3

#Load your custom JSON file
input_json_file = "data/esuder_cc1.json"

with open(input_json_file, "r") as reader:
    # load the JSON data and store it in the variable json_level_pack
    json_level_pack = json.load(reader)


#Convert JSON data to CCLevelPack
new_level_pack = cc_classes.CCLevelPack()
for json_level in json_level_pack:
    new_level = cc_classes.CCLevel()
    new_level.level_number = json_level["level_number"]
    new_level.num_chips = json_level["num_chips"]
    new_level.time = json_level["time"]
    new_level.upper_layer = json_level["upper_layer"]

    for json_field in json_level["optional_fields"]:
        field_type = json_field["field_type"]
        if field_type == "hint":
            new_hint_field = cc_classes.CCMapHintField(json_field["hint"])
            new_level.add_field(new_hint_field)
        elif field_type == "title":
            new_title_field = cc_classes.CCMapTitleField(json_field["title"])
            new_level.add_field(new_title_field)
        elif field_type == "password":
            new_password_field = cc_classes.CCEncodedPasswordField(json_field["password"])
            new_level.add_field(new_password_field)
        elif field_type == "monster":
            monsters = []
            json_monster_list = json_field["monsters"]
            for json_monster in json_monster_list:
                x = json_monster["x"]
                y = json_monster["y"]
                new_monster_coord = cc_classes.CCCoordinate(x, y)
                monsters.append(new_monster_coord)
            new_monster_field = cc_classes.CCMonsterMovementField(monsters)
            print("made new monster field")
            print(new_monster_field)
            new_level.add_field(new_monster_field)

    new_level_pack.add_level(new_level)

#print(new_level_pack)

cc_dat_utils.write_cc_level_pack_to_dat(new_level_pack, "data/esuder_cc1.dat")
#test_dat = cc_dat_utils.make_cc_level_pack_from_dat("data/esuder_cc1.dat")
#print(test_dat)