from location import Location

ENEMY_FLAG = "enemy"
NPC_FLAG = "npc"
INTERACT_FLAG = "interact"

home = Location(0, "Home")
town = Location(1, "Town Square")
cemetery = Location(2, "Cemetery")
alch_house = Location(3, "Alchemist's House")
alch_garden = Location(4, "Alchemist's Garden")
farm = Location(5, "Farmland")
forrest = Location(6, "Forrest")

home.south = town

town.north = home
town.east = alch_house
town.south = farm
town.west = cemetery

cemetery.east = town

alch_house.west = town
alch_house.east = alch_garden

alch_garden.west = alch_house

farm.north = town
farm.south = forrest

forrest.north = farm

home.description = "Your home. It's not much to speak of, but it is very dear to you."

town.description = "You see a fountain in the center. The town's folk meander about."

cemetery.description = "There are several rows of gravestones, most of which are in poor condition. " \
                       "The dirt beneath one of the gravestones opens up and a skeleton pops out!"

alch_house.description = "You see a small hut surrounded by many plants. A small man is sitting in his" \
                         " rocking chair as he examines a pile of flowers one by one. He looks up at" \
                         " with a quizzical look on his face."

alch_garden.description = "The alchemist's garden is huge, with a wide variety of plants. There" \
                          " is a particularly aromatic flower that you can't quite pinpoint" \
                          " the smell of. Suddenly, a spider jumps out at you!"

farm.description = "The farms are full of wheat and corn. Cows graze quietly off in the distance."

forrest.description = "The forrest is dank, pressing in around you. There are faint scraping sounds nearby. " \
                      "You think you hear a murmuring of voices down the path."

cemetery.contents.append(ENEMY_FLAG)
alch_house.contents.append(NPC_FLAG)
alch_garden.contents.append(ENEMY_FLAG)
forrest.contents.append(INTERACT_FLAG)

