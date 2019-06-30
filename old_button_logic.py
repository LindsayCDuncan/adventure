# def loc_bools(self):
#     if gm.PLAYER.current_loc.north is not None:
#         self.master.loc_has_north.set(True)
#     else:
#         self.master.loc_has_north.set(False)
#
#     if gm.PLAYER.current_loc.east is not None:
#         self.master.loc_has_east.set(True)
#     else:
#         self.master.loc_has_east.set(False)
#
#     if gm.PLAYER.current_loc.south is not None:
#         self.master.loc_has_south.set(True)
#     else:
#         self.master.loc_has_south.set(False)
#
#     if gm.PLAYER.current_loc.west is not None:
#         self.master.loc_has_west.set(True)
#     else:
#         self.master.loc_has_west.set(False)
#
#
#
#         south_btn["command"] = lambda loc = gm.PLAYER.current_loc.south: move(move_to_loc=loc)
#         north_btn["command"] = lambda loc = gm.PLAYER.current_loc.north: move(move_to_loc=loc)
#         east_btn["command"] = lambda loc = gm.PLAYER.current_loc.east: move(move_to_loc=loc)
#         west_btn["command"] = lambda loc = gm.PLAYER.current_loc.west: move(move_to_loc=loc)
#
#         def trace_north(*args):
#             if self.master.loc_has_north.get():
#                 north_btn.config(state=tk.NORMAL)
#             else:
#                 north_btn.config(state=tk.DISABLED)
#
#         def trace_east(*args):
#             if self.master.loc_has_east.get():
#                 east_btn.config(state=tk.NORMAL)
#             else:
#                 east_btn.config(state=tk.DISABLED)
#
#         def trace_south(*args):
#             if self.master.loc_has_south.get():
#                 south_btn.config(state=tk.NORMAL)
#             else:
#                 south_btn.config(state=tk.DISABLED)
#
#         def trace_west(*args):
#             if self.master.loc_has_west.get():
#                 west_btn.config(state=tk.NORMAL)
#             else:
#                 west_btn.config(state=tk.DISABLED)
#
#         self.master.loc_has_north.trace("w", trace_north)
#         self.master.loc_has_east.trace("w", trace_east)
#         self.master.loc_has_south.trace("w", trace_south)
#         self.master.loc_has_west.trace("w", trace_west)
#
#
#         def move(move_to_loc):
#             gm.move_player(move_to_loc)
#             # self.master.current_location.set(gm.PLAYER.current_loc)
#             # elf.master.location_description.set(gm.PLAYER.current_loc.description)
#             self.loc_bools()
#
#             print(gm.PLAYER.current_loc)
#             print(gm.PLAYER.current_loc.north)
#
#         def init_loc_bools(self):
#             self.master.loc_has_north.set(False)
#             self.master.loc_has_east.set(False)
#             self.master.loc_has_south.set(False)
#             self.master.loc_has_west.set(False)
#
#         self.loc_has_north = tk.BooleanVar()
#         self.loc_has_east = tk.BooleanVar()
#         self.loc_has_south = tk.BooleanVar()
#         self.loc_has_west = tk.BooleanVar()