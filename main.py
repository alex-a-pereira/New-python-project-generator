"""
Author & sole contributor:
Alex Pereira
Alex-a-pereira@outlook.com

See README.md for more info

"""
import os
import time
import ntpath
import tkinter as tk
import sqlite3

# this env variable set to 1 to create the venv w/ a script
os.environ["PIPENV_IGNORE_VIRTUALENVS"] = "1"


def check_paths(new_project, new_venv):
    conn = sqlite3.connect('paths.db')
    curs = conn.cursor()

    curs.execute("SELECT * FROM paths")
    table = curs.fetchone()
    old_project = table[0][1]
    old_venv = table[1][1]

    if new_project != old_project:
        update(new_project, 0)

    if new_venv != old_venv:
        update(new_venv, 1)

    return 0




def create_table():
    conn = sqlite3.connect('paths.db')
    curs = conn.cursor()

    curs.execute("CREATE TABLE IF NOT EXISTS paths (ID int, paths VARCHAR(255))")

    conn.commit()
    conn.close()


def insert(id_key, path):
    conn = sqlite3.connect('paths.db')
    curs = conn.cursor()

    curs.execute("INSERT INTO paths VALUES (?, ?)", (id_key, path))

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('paths.db')
    curs = conn.cursor()

    curs.execute("SELECT * FROM paths")

    rows = (curs.fetchall())
    conn.close()

    return rows


def update(id_key, path):
    conn = sqlite3.connect('paths.db')
    curs = conn.cursor()

    if os.path.isdir(path) is False:
        return 1


    curs.execute("UPDATE store SET path='?' WHERE id=?", (path, id_key))

    conn.commit()
    conn.close()




"""
create_table()

insert(0, "D:\\~Users\\alex\\Coding\\Python")
insert(1, "C:\\Users\\alex\\.virtualenvs")

print(view())
"""