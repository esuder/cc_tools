import cc_dat_utils
import cc_classes

#Part 3

#Load your custom JSON file
#with open("data/esuder_cc1.json", "r") as reader:
#    level_pack_json_data = json.load(reader)


#Convert JSON data to CCLevelPack
new_level_pack = cc_classes.CCLevelPack()
new_level = cc_classes.CCLevel()
new_level_pack.add_level(new_level)
print(new_level_pack)


#?


#Save converted data to DAT file
#cc_dat_utils.write_cc_level_pack_to_dat ("data/esuder_cc1.dat")
