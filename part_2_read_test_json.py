import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data.json) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()



    # Get the games array by looping through the the JSON data
    games = test_json_data["games"]

    # Iterate through the games array
    for game in games:
        # Create a new platform object with the "platform name" and "launch year"
        new_platform = test_data.Platform(game["platform name"], game["launch year"])
        # Create a new Game object by reading the title, the new_platform object, and the year
        new_game = test_data.Game(game["title"], new_platform, game["year"])
        # Add the Game object to the game_library
        game_library.add_game(new_game)

    return game_library



#Part 2

input_json_file = "data/test_data.json"
#Open the file specified by json_file_name (test_data.json)
with open(input_json_file, "r") as reader:
    # load the JSON data and store it in the variable test_json_data
    test_json_data = json.load(reader)


#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
game_library = make_game_library_from_json(test_json_data)


#Print out the resulting GameLibrary data using print()
print(game_library)

