from player import Player
import json
from player import PlayerJSONEncoder
from location import Location
from enemy import Enemy
from os import path


PLAYER = None
WORLD = dict()
ENEMY = None


def start_game(player_name):
    """" Initialize player character and load game world. """
    global PLAYER
    init_locations_from_file()
    PLAYER = Player(location=WORLD[1], name=player_name)


def move_player(location_direction):
    """ Check location string and move player if location exists. Return whether movement occurred. """
    global PLAYER
    global ENEMY

    if location_direction == "north"and PLAYER.current_loc.north:
        new_location = WORLD[PLAYER.current_loc.north]

    elif location_direction == "east" and PLAYER.current_loc.east:
        new_location = WORLD[PLAYER.current_loc.east]

    elif location_direction == "south" and PLAYER.current_loc.south:
        new_location = WORLD[PLAYER.current_loc.south]

    elif location_direction == "west" and PLAYER.current_loc.west:
        new_location = WORLD[PLAYER.current_loc.west]

    else:
        return False

    PLAYER.change_location(new_location)
    PLAYER.reset_current_health()

    # Instantiate an enemy if new location contains the enemy flag
    if PLAYER.current_loc.has_enemy:
        ENEMY = Enemy(other=PLAYER)

    return True


def check_location_interest():
    """ Return location contents as a string. """
    global PLAYER
    location = PLAYER.current_loc
    if location.has_enemy:
        return "enemy"
    if location.has_npc:
        return "npc"
    if location.has_investigate:
        return "investigate"
    return "nothing"


def check_loc_north():
    if PLAYER.current_loc.north:
        return True
    return False


def check_loc_east():
    if PLAYER.current_loc.east:
        return True
    return False


def check_loc_south():
    if PLAYER.current_loc.south:
        return True
    return False


def check_loc_west():
    if PLAYER.current_loc.west:
        return True
    return False


def attack():
    """ Player and enemy attack each other. Message holds outcomes of interaction. """
    global PLAYER
    global ENEMY
    player_leveled = False

    if ENEMY is None:
        message = "There are no enemies here.\n"

    else:
        PLAYER.attack(ENEMY)
        player_attack_msg = f"{PLAYER.name} attacks {ENEMY.name} for {PLAYER.damage} damage.\n"

        # Enemy is alive after player attack
        if ENEMY.is_alive():
            ENEMY.attack(PLAYER)
            enemy_attack_msg = f"{ENEMY.name} attacks {PLAYER.name} for {ENEMY.damage} damage.\n"
            message = f"{player_attack_msg}{enemy_attack_msg}"

        # Enemy is dead after player attack
        else:
            PLAYER.gain_exp(ENEMY.exp_reward)
            enemy_death = f"{ENEMY.name} has died!\n"
            exp_msg = f"{PLAYER.name} gains {ENEMY.exp_reward} experience!\n"
            message = f"{player_attack_msg}{enemy_death}{exp_msg}"

            if PLAYER.ready_to_level():
                PLAYER.level_up()
                lvl_msg = f"{PLAYER.name} has leveled up!\n"
                message = f"{player_attack_msg}{enemy_death}{exp_msg}{lvl_msg}"
                player_leveled = True

            ENEMY = None

    return message, player_leveled


def talk():
    """ Talk interaction with NPC. Not yet fully implemented. """
    return "The old man gives you a hard stare, then turns back to his work.\n"


def init_locations_from_file():
    """ Initialize world from location json file. """
    global WORLD
    with open("locations.json", "r") as json_file:
        data = json.load(json_file)
        for loc in data:
            new_loc = Location(loc["id"], loc["name"])
            new_loc.description = loc["description"]
            new_loc.has_enemy = loc["enemy"]
            new_loc.has_npc = loc["npc"]
            new_loc.has_investigate = loc["investigate"]
            new_loc.north = loc["north"]
            new_loc.east = loc["east"]
            new_loc.south = loc["south"]
            new_loc.west = loc["west"]
            WORLD[new_loc.id] = new_loc


def save_game():
    """ Save player stats. """
    global PLAYER
    try:
        with open("player_data.json", "w") as player_file:
            json.dump(PLAYER, player_file, cls=PlayerJSONEncoder)
            return True
    except IOError:
        return False


def load_game():
    """ Load player stats from file. """
    global PLAYER
    global WORLD
    init_locations_from_file()

    if path.exists("player_data.json"):
        try:
            with open("player_data.json", "r") as player_file:
                data = json.load(player_file)
                PLAYER = Player(location=WORLD[1], name=data["name"])
                PLAYER.max_health = data["max_health"]
                PLAYER.current_health = data["current_health"]
                PLAYER.damage = data["damage"]
                PLAYER.alive = data["alive"]
                PLAYER.level = data["level"]
                PLAYER.max_exp = data["max_exp"]
                PLAYER.current_exp = data["current_exp"]
            return True
        except TypeError:
            return False
    else:
        return False




