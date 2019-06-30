from player import Player
from enemy import Enemy
import world

ENEMY_FLAG = "enemy"
NPC_FLAG = "npc"

player = Player(world.home, "Kitten")
move_to = ""

while True:
    print(player.current_loc.description)
    move_to = input("Move to new location: NSEW ").upper()

    if move_to == "S" and player.current_loc.south:
        player.change_location(player.current_loc.south)
    if move_to == "N" and player.current_loc.north:
        player.change_location(player.current_loc.north)
    if move_to == "E" and player.current_loc.east:
        player.change_location(player.current_loc.east)
    if move_to == "W" and player.current_loc.west:
        player.change_location(player.current_loc.west)

    if move_to == "Q":
        break