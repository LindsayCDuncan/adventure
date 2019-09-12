""" Button click and attack sounds: by SoundBible.com
    'Patakas World' by www.dl-sounds.com
    'The Island of Dr. Sinister' by Eric Matyas www.soundimage.org
"""

import tkinter as tk
import game_manager as gm
from pygame import mixer
import time
from tkinter import messagebox


class GUIApp(tk.Tk):
    """ Main GUI application to hold other frame classes. """
    def __init__(self):
        """ Initialize the main frame, variables, and game state. The main frame is a place holder for the underlying frames
            to support frame changes.
        """
        tk.Tk.__init__(self)
        self.center_screen()
        self.resizable(False, False)
        self.title("RPG")
        self.current_frame = None

        # Menu bar is initialized but will not show up until frame changes to game screen
        self.menu_bar = tk.Menu(self)

        self.player_name = "Unnamed Hero"
        self.player_level = tk.IntVar()
        self.player_max_health = tk.IntVar()
        self.player_current_health = tk.IntVar()
        self.total_health = tk.StringVar()
        self.player_damage = tk.IntVar()
        self.player_max_exp = tk.IntVar()
        self.player_current_exp = tk.IntVar()
        self.current_location = tk.StringVar()
        self.location_description = tk.StringVar()

        self.loc_has_north = tk.BooleanVar(False)
        self.loc_has_east = tk.BooleanVar(False)
        self.loc_has_south = tk.BooleanVar(False)
        self.loc_has_west = tk.BooleanVar(False)

        self.interact_text = tk.StringVar(value="")

        # Set up mixer and sounds
        mixer.init()
        self.btn_sound = mixer.Sound("button_click.wav")
        self.attack_btn_sound = mixer.Sound("attack_sound.wav")
        self.lvl_up_sound = mixer.Sound("level_up.wav")
        self.play_music()

        # Start screen is the first screen to display
        self.replace_frame(StartScreen)

    def add_menu(self):
        """ Options menu for game. Enables player to save and quit during gameplay. """
        filemenu = tk.Menu(self.menu_bar, tearoff=0)
        filemenu.add_command(label="Save", command=self.save_game)
        filemenu.add_command(label="Quit", command=self.quit)
        self.menu_bar.add_cascade(label="Options", menu=filemenu)
        self.config(menu=self.menu_bar)

    def save_game(self):
        if gm.save_game():
            messagebox.showinfo("Saved.", "Game saved successfully!")
        else:
            messagebox.showinfo("Error.", "There was a problem saving the game.")

    def replace_frame(self, frame):
        """ Remove current frame and replace with the frame passed in."""
        new_frame = frame(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame

        # Change music on ending frame
        if isinstance(self.current_frame, EndScreen):
            self.play_end_music()

        self.current_frame.pack()

    def center_screen(self):
        """ Set the main frame to the center of the monitor's screen."""
        width = 600
        height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coord = int((screen_width / 2) - (width / 2))
        y_coord = int((screen_height / 2) - (height / 2))

        self.geometry(f"{width}x{height}+{x_coord}+{y_coord}")

    def play_music(self):
        """ Load music file for main game play and set it to loop indefinitely. """
        mixer.music.load("PatakasWorld.wav")
        mixer.music.set_volume(.3)
        mixer.music.play(loops=-1)

    def play_end_music(self):
        """ Load music for end screen. """
        mixer.music.fadeout(1000)
        mixer.music.load("The_Island_of_Dr_Sinister.mp3")
        mixer.music.set_volume(.4)
        mixer.music.play(loops=-1)

    def attack_sound(self):
        self.attack_btn_sound.set_volume(.4)
        mixer.Sound.play(self.attack_btn_sound)

    def button_sound(self):
        self.btn_sound.set_volume(.4)
        mixer.Sound.play(self.btn_sound)

    def levelup_sound(self):
        self.lvl_up_sound.set_volume(.4)
        mixer.Sound.play(self.lvl_up_sound)

    def quit_button(self):
        """ Quit the application. """
        self.button_sound()
        time.sleep(.5)
        self.quit()

    def update_variables(self):
        """ Update GUI variables with player information. """
        self.player_level.set(gm.PLAYER.level)
        self.player_max_health.set(gm.PLAYER.max_health)
        self.player_current_health.set(gm.PLAYER.current_health)
        self.total_health.set(f"{self.player_current_health.get()} / {self.player_max_health.get()}")
        self.player_damage.set(gm.PLAYER.damage)
        self.player_max_exp.set(gm.PLAYER.max_exp)
        self.player_current_exp.set(gm.PLAYER.current_exp)
        self.current_location.set(gm.PLAYER.current_loc)
        self.location_description.set(gm.PLAYER.current_loc.description)


class StartScreen(tk.Frame):
    """ First frame. Welcomes the player and starts the game. """
    def __init__(self, master):
        """ Initialize welcome frame. Take in character name and start game on button click. """
        tk.Frame.__init__(self, master)

        self.top_frame = tk.Frame(self)
        self.middle_frame = tk.Frame(self)
        self.bottom_frame = tk.Frame(self)

        self.welcome_label = tk.Label(self.top_frame, text="WELCOME TO THIS AMAZING ADVENTURE!", font=("Helvetica", 14))
        self.welcome_label.pack(side=tk.TOP, pady=[100, 50])

        self.entry_label = tk.Label(self.middle_frame, text="Enter your character name or load a saved game:")
        self.entry_label.pack(side=tk.LEFT, padx=5, pady=30)

        self.player_name_entered = tk.StringVar()
        self.player_entry = tk.Entry(self.middle_frame, width=40, textvariable=self.player_name_entered)
        self.player_entry.pack(side=tk.LEFT, padx=5, pady=30)
        self.player_entry.focus_set()

        self.start_button = tk.Button(self.bottom_frame, text="Start", width=10, command=self.start_button_click)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.load_button = tk.Button(self.bottom_frame, text="Load", width=10, command=self.load_button_click)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.quit_button = tk.Button(self.bottom_frame, text="Quit", width=10, command=master.quit_button)
        self.quit_button.pack(side=tk.LEFT, padx=5)

        self.top_frame.pack(side=tk.TOP)
        self.middle_frame.pack(side=tk.TOP)
        self.bottom_frame.pack(side=tk.TOP)

    def start_button_click(self):
        """ Initialize game in game manager and update GUI. """
        # Strip player input to disallow blank names
        if self.player_name_entered.get().strip():
            self.master.player_name = self.player_name_entered.get()

        gm.start_game(self.master.player_name)
        self.master.update_variables()
        self.master.button_sound()
        self.master.replace_frame(GameScreen)

    def load_button_click(self):
        """ Load game in game manager and update GUI."""
        if gm.load_game():
            self.master.update_variables()
            self.master.player_name = gm.PLAYER.name
            self.master.button_sound()
            self.master.replace_frame(GameScreen)
        else:
            messagebox.showinfo("No saved game", "Start a new game.")


class GameScreen(tk.Frame):
    """ Second frame. Holds main game view. """
    def __init__(self, master):
        """ Initialize frame and set sub-frames. """
        tk.Frame.__init__(self, master)

        self.master.add_menu()

        self.player_frame = tk.Frame(self, width=300, height=300, bd=3, relief=tk.SUNKEN)
        self.player_frame.grid(row=0, column=0)
        self.player_frame.pack_propagate(False)
        self.player_labels(self.player_frame)

        self.location_frame = tk.Frame(self, width=300, height=300, bd=3, relief=tk.SUNKEN)
        self.location_frame.grid(row=0, column=1)
        self.location_frame.pack_propagate(False)
        self.location_info(self.location_frame)

        self.combat_frame = tk.Frame(self, width=300, height=300, bd=3, relief=tk.SUNKEN)
        self.combat_frame.grid(row=1, column=0)
        self.combat_frame.pack_propagate(False)
        self.log_text = tk.Text(self.combat_frame, width=200, height=200, wrap="word", font=("Helvetica", 9))
        self.combat_log(self.combat_frame)

        self.movement_frame = tk.Frame(self, width=300, height=300, bd=3, relief=tk.SUNKEN)
        self.movement_frame.grid(row=1, column=1)
        self.movement_buttons(self.movement_frame)

    def player_labels(self, frame):
        """ Initialize labels to hold player information in the character frame. """
        char_frame = tk.LabelFrame(frame, width=260, height=260, text="Character Information", font=("Helvetica", 12))
        char_frame.pack_propagate(False)

        label_frame = tk.Frame(char_frame, width=130, height=260)
        data_frame = tk.Frame(char_frame, width=130, height=260)

        tk.Label(label_frame, text="Name:").pack(side=tk.TOP, padx=30, pady=[0, 5], anchor=tk.NW)
        tk.Label(data_frame, text=self.master.player_name).pack(side=tk.TOP, padx=10, pady=[0, 5], anchor=tk.NW)
        tk.Label(label_frame, text="Level:").pack(side=tk.TOP, padx=30, pady=5, anchor=tk.NW)
        tk.Label(data_frame, textvariable=self.master.player_level).pack(side=tk.TOP, padx=10, pady=5, anchor=tk.NW)
        tk.Label(label_frame, text="Health:").pack(side=tk.TOP, padx=30, pady=5, anchor=tk.NW)
        tk.Label(data_frame, textvariable=self.master.total_health).pack(side=tk.TOP, padx=10, pady=5, anchor=tk.NW)
        tk.Label(label_frame, text="Damage:").pack(side=tk.TOP, padx=30, pady=[5, 50], anchor=tk.NW)
        tk.Label(data_frame, textvariable=self.master.player_damage).pack(side=tk.TOP, padx=10, pady=[5, 50], anchor=tk.NW)

        label_frame.pack(side=tk.LEFT)
        data_frame.pack(side=tk.LEFT)
        char_frame.pack(pady=20)

    def location_info(self, frame):
        """ Initialize the location frame to hold game-world location information. """
        description_frame = tk.Frame(frame, height=150, width=250, bd=2, relief=tk.GROOVE)
        description_frame.pack_propagate(False)
        tk.Label(frame, textvariable=self.master.current_location, font=("Helvetica", 12)).pack(side=tk.TOP, pady=[15, 0])
        tk.Label(description_frame, textvariable=self.master.location_description, justify=tk.CENTER,
                 wraplength=230, anchor=tk.NW, pady=5, padx=10).pack(side=tk.TOP, pady=5)
        description_frame.pack(side=tk.TOP, pady=10)
        interact_btn = tk.Button(frame, textvariable=self.master.interact_text, width=20)

        def button_commands():
            """ Set button commands according to button text. """
            if self.master.interact_text.get() == "Attack":
                interact_btn["command"] = self.btn_attack
            elif self.master.interact_text.get() == "Talk":
                interact_btn["command"] = self.btn_talk
            elif self.master.interact_text.get() == "Investigate":
                interact_btn["command"] = self.btn_investigate

        def interact_btn_visibility(*args):
            """ Unpack button if no interaction is available in a given game-world location. """
            if self.master.interact_text.get() == "":
                interact_btn.pack_forget()
            else:
                button_commands()
                interact_btn.pack(side=tk.TOP, pady=10)

        # Set initial button visibility
        interact_btn_visibility()
        self.master.interact_text.trace("w", interact_btn_visibility)

    def btn_talk(self):
        """ Initiate npc talking interaction. """
        self.master.button_sound()
        message = gm.talk()
        self.update_combat_log_text(message=message)

    def btn_investigate(self):
        """ Initiate end game state. """
        self.master.button_sound()
        self.master.replace_frame(EndScreen)

    def btn_attack(self):
        """ Initiate attack interaction. Update GUI. """
        self.master.attack_sound()
        attack_msg, player_leveled = gm.attack()
        self.update_combat_log_text(message=attack_msg)

        if player_leveled:
            self.master.levelup_sound()

        self.master.update_variables()

    def update_combat_log_text(self, message):
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.insert(tk.END, message)
        self.log_text.see(tk.END)
        self.log_text.configure(state=tk.DISABLED)

    def interact_btn_text(self, text):
        """ Receive string describing location's content. Set button text variable according to content. """
        if text == "enemy":
            self.master.interact_text.set("Attack")
        elif text == "npc":
            self.master.interact_text.set("Talk")
        elif text == "investigate":
            self.master.interact_text.set("Investigate")
        else:
            self.master.interact_text.set("")

    def combat_log(self, frame):
        """ Initialize combat log frame with scroll bar. """
        # Disable text box so user cannot enter input
        self.log_text.configure(state=tk.DISABLED)
        scroll_bar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text['yscrollcommand'] = scroll_bar.set
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.pack(side=tk.TOP)

    def movement_buttons(self, frame):
        """ Initialize movement frame. """
        north_btn = tk.Button(frame, text="North", width=10)
        east_btn = tk.Button(frame, text="East", width=10)
        west_btn = tk.Button(frame, text="West", width=10)
        south_btn = tk.Button(frame, text="South", width=10)

        # define trace functions for movement buttons
        def trace_north(*args):
            if self.master.loc_has_north.get():
                north_btn.config(state=tk.NORMAL)
            else:
                north_btn.config(state=tk.DISABLED)

        def trace_east(*args):
            if self.master.loc_has_east.get():
                east_btn.config(state=tk.NORMAL)
            else:
                east_btn.config(state=tk.DISABLED)

        def trace_south(*args):
            if self.master.loc_has_south.get():
                south_btn.config(state=tk.NORMAL)
            else:
                south_btn.config(state=tk.DISABLED)

        def trace_west(*args):
            if self.master.loc_has_west.get():
                west_btn.config(state=tk.NORMAL)
            else:
                west_btn.config(state=tk.DISABLED)

        # Set trace on movement buttons to disable buttons if movement is not allowed in that direction
        self.master.loc_has_north.trace("w", trace_north)
        self.master.loc_has_east.trace("w", trace_east)
        self.master.loc_has_south.trace("w", trace_south)
        self.master.loc_has_west.trace("w", trace_west)

        # Update locations bools after trace so that buttons are properly enabled/disabled
        self.location_bools()

        def move(move_to_loc):
            """ Send movement as a string to game manager and update GUI if movement is allowed. """
            self.master.button_sound()
            if gm.move_player(move_to_loc):
                self.location_bools()
                self.master.update_variables()
                self.interact_btn_text(gm.check_location_interest())

        north_btn["command"] = lambda loc="north": move(move_to_loc=loc)
        east_btn["command"] = lambda loc="east": move(move_to_loc=loc)
        south_btn["command"] = lambda loc="south": move(move_to_loc=loc)
        west_btn["command"] = lambda loc="west": move(move_to_loc=loc)

        north_btn.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        east_btn.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
        west_btn.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
        south_btn.place(relx=0.5, rely=.6, anchor=tk.CENTER)

    def location_bools(self):
        """ Set location booleans according to player's current location's surroundings. """
        self.master.loc_has_north.set(gm.check_loc_north())
        self.master.loc_has_east.set(gm.check_loc_east())
        self.master.loc_has_south.set(gm.check_loc_south())
        self.master.loc_has_west.set(gm.check_loc_west())


class EndScreen(tk.Frame):
    """ Third and final frame. End the game and quit application. """
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        ending_message = "You proceed down the path.\nA group of bandits jump out and bop you on the head.\n" \
                         "Everything turns to black.\n\nIs this the end of your adventure?"
        credits = "Sound Credits:\nButton click and attack: SoundBible.com\n" \
                  "'Patakas World' by www.dl-sounds.com\n'The Island of Dr. Sinister' by Eric Matyas www.soundimage.org"

        self.ending_label = tk.Label(self, text=ending_message, font=("Helvetica", 13)).pack(side=tk.TOP, pady=[100, 25])
        self.goodbye_label = tk.Label(self, text="Goodbye for now...", font=("Helvetica", 16)).pack(side=tk.TOP, pady=[25, 50])
        self.quit_button = tk.Button(self, text="Quit", width=10, command=master.quit_button).pack(side=tk.TOP)
        self.sound_credits = tk.Label(self, text=credits, font=("Helvetica", 7)).pack(side=tk.TOP, pady=[100, 0])


if __name__ == '__main__':
    app = GUIApp()
    app.mainloop()
