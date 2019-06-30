import tkinter as tk
import game_manager as gm


class GUIApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.center_screen()
        self.resizable(False, False)
        self.title("RPG")
        self.current_frame = None

        self.player_name = "Bob"
        self.player_level = tk.IntVar()
        self.player_max_health = tk.IntVar()
        self.player_current_health = tk.IntVar()
        self.player_damage = tk.IntVar()
        self.player_max_exp = tk.IntVar()
        self.player_current_exp = tk.IntVar()
        self.current_location = tk.StringVar()
        self.location_description = tk.StringVar()

        self.replace_frame(StartScreen)

    def replace_frame(self, frame):
        new_frame = frame(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()

    def center_screen(self):
        width = 600
        height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coord = int((screen_width / 2) - (width / 2))
        y_coord = int((screen_height / 2) - (height / 2))

        self.geometry(f"{width}x{height}+{x_coord}+{y_coord}")


class StartScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.top_frame = tk.Frame(self)
        self.middle_frame = tk.Frame(self)
        self.bottom_frame = tk.Frame(self)

        self.welcome_label = tk.Label(self.top_frame, text="WELCOME TO THIS RPG!", font=("Helvetica", 14))
        self.welcome_label.pack(side=tk.TOP, pady=[100, 50])

        self.entry_label = tk.Label(self.middle_frame, text="Enter your character name:")
        self.entry_label.pack(side=tk.LEFT, padx=5, pady=30)

        self.player_name_entered = tk.StringVar()
        self.player_entry = tk.Entry(self.middle_frame, width=40, textvariable=self.player_name_entered)
        self.player_entry.pack(side=tk.LEFT, padx=5, pady=30)
        self.player_entry.focus_set()

        self.start_button = tk.Button(self.bottom_frame, text="Start", width=10,
                                      command=self.start_button_click)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.quit_button = tk.Button(self.bottom_frame, text="Quit", width=10, command=master.quit)
        self.quit_button.pack(side=tk.LEFT, padx=5)

        self.top_frame.pack(side=tk.TOP)
        self.middle_frame.pack(side=tk.TOP)
        self.bottom_frame.pack(side=tk.TOP)

    def start_button_click(self, event=None):
        if self.player_name_entered.get():
            self.master.player_name = self.player_name_entered.get()

        gm.start_game(self.master.player_name)

        self.master.player_level.set(gm.PLAYER.level)
        self.master.player_max_health.set(gm.PLAYER.max_health)
        self.master.player_current_health.set(gm.PLAYER.current_health)
        self.master.player_damage.set(gm.PLAYER.damage)
        self.master.player_max_exp.set(gm.PLAYER.max_exp)
        self.master.player_current_exp.set(gm.PLAYER.current_exp)
        self.master.current_location.set(gm.PLAYER.current_loc)
        self.master.location_description.set(gm.PLAYER.current_loc.description)

        self.master.replace_frame(GameScreen)


class GameScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
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
        self.combat_log(self.combat_frame)

        self.movement_frame = tk.Frame(self, width=300, height=300, bd=3, relief=tk.SUNKEN)
        self.movement_frame.grid(row=1, column=1)
        self.movement_buttons(self.movement_frame)

    def player_labels(self, frame):
        char_frame = tk.LabelFrame(frame, width=260, height=260, text="Character Information", font=("Helvetica", 12))
        char_frame.pack_propagate(False)

        label_frame = tk.Frame(char_frame, width=130, height=260)
        data_frame = tk.Frame(char_frame, width=130, height=260)

        tk.Label(label_frame, text="Name:").pack(side=tk.TOP, padx=30, pady=[0, 5], anchor=tk.NW)
        tk.Label(data_frame, text=self.master.player_name).pack(side=tk.TOP, padx=10, pady=[0, 5], anchor=tk.NW)
        tk.Label(label_frame, text="Level:").pack(side=tk.TOP, padx=30, pady=5, anchor=tk.NW)
        tk.Label(data_frame, textvariable=self.master.player_level).pack(side=tk.TOP, padx=10, pady=5, anchor=tk.NW)
        tk.Label(label_frame, text="Health:").pack(side=tk.TOP, padx=30, pady=5, anchor=tk.NW)
        tk.Label(data_frame, textvariable=self.master.player_max_health).pack(side=tk.TOP, padx=10, pady=5, anchor=tk.NW)
        tk.Label(label_frame, text="Damage:").pack(side=tk.TOP, padx=30, pady=[5, 50], anchor=tk.NW)
        tk.Label(data_frame, textvariable=self.master.player_damage).pack(side=tk.TOP, padx=10, pady=[5, 50], anchor=tk.NW)

        label_frame.pack(side=tk.LEFT)
        data_frame.pack(side=tk.LEFT)
        char_frame.pack(pady=20)

    def location_info(self, frame):
        description_frame = tk.Frame(frame, height=150, width=250, bd=2, relief=tk.GROOVE)
        description_frame.pack_propagate(False)
        tk.Label(frame, textvariable=self.master.current_location, font=("Helvetica", 12)).pack(side=tk.TOP, pady=[15, 0])
        tk.Label(description_frame, textvariable=self.master.location_description, justify=tk.CENTER,
                 wraplength=230, anchor=tk.NW, pady=5, padx=10).pack(side=tk.TOP, pady=5)
        description_frame.pack(side=tk.TOP, pady=10)
        tk.Button(frame, text="Interact", width=20).pack(side=tk.TOP, pady=10)

    def combat_log(self, frame):
        log_text = tk.Text(frame, width=200, height=200, wrap="word")
        log_text.insert("1.0", "Combat information here\n")

        log_text.configure(state=tk.DISABLED)
        scroll_bar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=log_text.yview)
        log_text['yscrollcommand'] = scroll_bar.set
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        log_text.pack(side=tk.TOP)

    def movement_buttons(self, frame):

        north_btn = tk.Button(frame, text="North", width=10)
        east_btn = tk.Button(frame, text="East", width=10)
        west_btn = tk.Button(frame, text="West", width=10)
        south_btn = tk.Button(frame, text="South", width=10)

        north_btn.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        east_btn.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
        west_btn.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
        south_btn.place(relx=0.5, rely=.6, anchor=tk.CENTER)


class EndScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.goodbye_label = tk.Label(self, text="GOODBYE!", font=("Helvetica", 16)).pack(side=tk.TOP, pady=100)
        self.quit_button = tk.Button(self, text="Quit", width=10, command=master.quit).pack(side=tk.TOP)


app = GUIApp()
app.mainloop()
