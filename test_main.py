import tkinter as tk


class MainFrame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("RPG")
        self.geometry("600x600")
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for frame in (StartScreen, GameScreen, EndScreen):
            frame_name = frame.__name__
            new_frame = frame(master=container, controller=self)
            self.frames[frame_name] = new_frame
            new_frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.change_frame("StartScreen")

    def change_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


class StartScreen(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.top_frame = tk.Frame(self)
        self.middle_frame = tk.Frame(self)
        self.bottom_frame = tk.Frame(self)

        self.welcome_label = tk.Label(self.top_frame, text="WELCOME TO THIS RPG!").pack(side=tk.TOP, pady=100)

        self.entry_label = tk.Label(self.middle_frame, text="Enter your character name:").pack(side=tk.LEFT,
                                                                                               padx=5, pady=30)
        self.player_name = tk.StringVar()
        self.player_entry = tk.Entry(self.middle_frame, width=40, textvariable=self.player_name).pack(side=tk.LEFT,
                                                                                                      padx=5, pady=30)

        self.start_button = tk.Button(self.bottom_frame, text="Start", width=10,
                                      command=lambda: controller.change_frame("EndScreen")).pack(side=tk.LEFT, padx=5)
        self.quit_button = tk.Button(self.bottom_frame, text="Quit", width=10, command=master.quit).pack(side=tk.LEFT,
                                                                                                         padx=5)

        self.top_frame.pack(side=tk.TOP)
        self.middle_frame.pack(side=tk.TOP)
        self.bottom_frame.pack(side=tk.TOP)


class GameScreen(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.goodbye_label = tk.Label(self, text="GOODBYE!").pack(side=tk.TOP, pady=100)
        self.quit_button = tk.Button(self, text="Quit", width=10, command=master.quit).pack(side=tk.TOP)


class EndScreen(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.goodbye_label = tk.Label(self, text="GOODBYE!").pack(side=tk.TOP, pady=100)
        self.quit_button = tk.Button(self, text="Quit", width=10, command=master.quit).pack(side=tk.TOP)


def main():
    app = MainFrame()
    app.mainloop()


main()

