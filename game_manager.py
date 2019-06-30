import world
from player import Player
from enemy import Enemy


PLAYER = None


def start_game(player_name):
    global PLAYER
    PLAYER = Player(location=world.home, name=player_name)


def move_player(new_location):
    global PLAYER
    PLAYER.change_location(new_location)

