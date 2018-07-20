import tkinter as tk
import backend


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

        self.name_label = tk.Label(self, text="New Project Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.StringVar()
        self.name_entry = tk.Entry(self, textvariable=self.name_entry)
        self.name_entry.grid(row=0, column=1)

        self.url_label = tk.Label(self, text="Remote URL (optional)")
        self.url_label.grid(row=1, column=0)
        self.url_entry = tk.StringVar()
        self.url_entry = tk.Entry(self, textvariable=self.url_entry)
        self.url_entry.grid(row=1, column=1)

        self.proj_label = tk.Label(self, text="Projects path")
        self.proj_label.grid(row=2, column=0)
        self.proj_entry = tk.StringVar()
        self.proj_entry = tk.Entry(self, textvariable=self.proj_entry)
        self.proj_entry.grid(row=2, column=1)

        self.venv_label = tk.Label(self, text="Virtual env path")
        self.venv_label.grid(row=3, column=0)
        self.venv_entry = tk.StringVar()
        self.venv_entry = tk.Entry(self, textvariable=self.venv_entry)
        self.venv_entry.grid(row=3, column=1)

        self.create = tk.Button(self, text="Create Project", command=self.create_project)
        self.create.grid(row=0, column=3)

        self.quit_button = tk.Button(self, text="QUIT", fg="red", command=root.destroy)

    def get_paths(self):
        paths = [self.proj_entry.get(), self.venv_entry.get()]
        print(paths)

    def create_project(self):
        backend.create(self.name_entry, self.proj_entry.get(), self.venv_entry.get())


def main():
    root = tk.Tk()
    app = Application(master=root)

    app.mainloop()


if __name__ == "main":
    main()



