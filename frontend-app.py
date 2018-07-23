import tkinter as tk
import backend


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, bg="#353b48")
        self.pack()

        self.defaults_paths = backend.get_dir_defaults()

        self.name_label = tk.Label(self, text="New Project Name", bg="#353b48", fg="#dcdde1", justify="left")
        self.name_label.grid(row=0, column=0, pady=2)
        self.name_entry = tk.StringVar()
        self.name_entry = tk.Entry(self, textvariable=self.name_entry, bg="#dcdde1", fg="#353b48", width=40)
        self.name_entry.grid(row=0, column=1, pady=2)

        self.url_label = tk.Label(self, text="Remote URL (optional)", bg="#353b48", fg="#dcdde1", justify="left")
        self.url_label.grid(row=1, column=0, pady=2)
        self.url_entry = tk.StringVar(self, value="*not yet functional*")
        self.url_entry = tk.Entry(self, textvariable=self.url_entry, bg="#dcdde1", fg="#353b48", width=40)
        self.url_entry.grid(row=1, column=1, pady=2)

        self.proj_label = tk.Label(self, text="Projects path", bg="#353b48", fg="#dcdde1", justify="left")
        self.proj_label.grid(row=2, column=0, pady=2)
        self.proj_entry = tk.StringVar(self, value=self.defaults_paths[0])
        self.proj_entry = tk.Entry(self, textvariable=self.proj_entry, bg="#dcdde1", fg="#353b48", width=40)
        self.proj_entry.grid(row=2, column=1, pady=2)

        self.venv_label = tk.Label(self, text="Virtual env path", bg="#353b48", fg="#dcdde1", justify="left")
        self.venv_label.grid(row=3, column=0, pady=2)
        self.venv_entry = tk.StringVar(self, value=self.defaults_paths[1])
        self.venv_entry = tk.Entry(self, textvariable=self.venv_entry, bg="#dcdde1", fg="#353b48", width=40)
        self.venv_entry.grid(row=3, column=1, pady=2)

        self.create = tk.Button(self, text="Create Project", bg="#dcdde1", fg="#353b48",  width=20,
                                height=2, command=self.create_project)
        self.create.grid(row=2, rowspan=2, column=3, pady=2, padx=5)

        self.quit_button = tk.Button(self, text="Quit", bg="#dcdde1", fg="#353b48", width=20, height=2,
                                     command=root.destroy)
        self.quit_button.grid(row=0, rowspan=2, column=3, pady=2, padx=5)

    def get_paths(self):
        paths = [self.proj_entry.get(), self.venv_entry.get()]
        print(paths)

    def create_project(self):
        backend.create_project(self.name_entry.get(), self.proj_entry.get(), self.venv_entry.get())


root = tk.Tk()
app = Application(master=root)

app.mainloop()


