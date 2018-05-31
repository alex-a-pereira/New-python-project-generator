"""
Author & sole contributor:
Alex Pereira
Alex--pereira@outlook.com

See README.md for more info

"""
import os
import time
import ntpath

project_name = project_folder = project_dir = venv_dir = ""

# this env variable set to 1 to create the venv w/ a script
os.environ["PIPENV_IGNORE_VIRTUALENVS"] = "1"


# this function exists so the user can specify whether they'd like to run
def askUser(input_string):

    while True:
        yesOrNo = input(input_string)
        if yesOrNo not in ("Y", "N"):
            print("Please input only Y or N")
            continue
        else:
            break
    return yesOrNo


# assemblePath is called to ask the user to specify a path for the current variable.
def assemblePath(message):
    # accept user's input to specify path
    while True:
        try:
            path = input(message)
            path = ntpath.abspath(path)  # will convert to a absolute path if not already
            if not ntpath.exists(path):
                raise FileNotFoundError  # if the path doesn't exist, raise this error
        except FileNotFoundError:
            print("Directory not found! Please try again.\ne.g. C:\\users\\username\\documents\\projects")
            continue
        break
    return path

def writeCredentials():

    global file_name
    file_name = "secrets.txt"
    file = open(file_name, "w+")

    file.truncate(0)
    file.write("Project directory:\n")
    file.write(assemblePath("Please specify your project directory: "))
    file.write("\n\nVirtual environment directory:\n")
    file.write(assemblePath("Please specify your virtual environment directory: "))

    file.close()
    # whenever I write to the file, I must then read it
    print("\n*** Please ensure directory locations below are valid ***\n")
    file = open(file_name, "r")
    print(file.read() + "\n")


def checkCredentials():

    global file_name
    global project_dir
    global venv_dir
    global project_name
    global project_folder

    print("Checking directory credentials...\n")
    time.sleep(1)

    file_name = "secrets.txt"
    file = open(file_name, "r")
    # try to open secrets.txt and if it doesn't exist, create one w/ open(name, "w+). In either case, open to read
    try:
        print(file.read())

    except FileNotFoundError:
        file = open(file_name, "w+")  # creates the file secrets.txt
        file.close()
        writeCredentials()

    print("\n*** Please ensure directory locations above are valid ***")
    print("*** Blank lines indicate blank credentials! ***\n")

    yesOrNo = askUser("Do you want to delete and re-enter credentials? Y or N: ")
    while yesOrNo == "Y":
        writeCredentials()
        yesOrNo = askUser("Delete and re-enter credentials? Y or N: ")

    file = open(file_name, "r")
    line_list = file.readlines()

    project_dir = line_list[1]
    project_dir = project_dir[:int(len(project_dir) - 1)]  # removes the "\n" from end of line

    venv_dir = line_list[4]

    # setting up default values for project_folder and project_name
    project_name = "Project 1"
    project_folder = ntpath.join(project_dir, project_name)


def createProject():

        global project_name
        global project_folder

        os.chdir(project_dir)  # change the working directory to the directory containing your project folders

        while True:  # loop until I create the project folder
            try:
                project_name = input("Specify project name: ")
                os.mkdir(project_name)
            except FileExistsError:
                print("Project already exists in " + project_dir + ". Try another project name: ")
                continue
            break
        # assign the variable project_folder to the new path and create a venv w/ cmd line
        project_folder = ntpath.join(project_dir, project_name)
        os.system(project_folder[:2] + " & cd " + project_folder + " & pipenv --python 3.6")

        # specify the project's virtual environment
        os.chdir(venv_dir)
        all_venvs = [d for d in os.listdir('.') if os.path.isdir(d)]
        project_venv = max(all_venvs, key=os.path.getmtime)
        venv_path = venv_dir + project_venv
        print("Project created.)

        os.chdir(project_folder)  # change working directory to the project folder


def installPackages():

    os.chdir(project_folder)

    while True:
        package_str = input("Specify packages to install, separated by a comma and a space: ")
        package_list = package_str.split(", ")

        for package in package_list:
            os.system(project_folder[:2] + " & cd " + project_folder + " & pipenv install " + package)

        print("\nOpening pipfile to review this project's installed packages ...\n")
        time.sleep(2)
        print("************************************************")
        pipfile = open(project_folder + "/Pipfile", "r")
        print(pipfile.read())
        print("************************************************")
        yesOrNo = askUser("Install more packages? Y or N: ")
        if yesOrNo == "N":
            break


def main():
    checkCredentials()

    # create a project??
    yesOrNo = askUser("Create a project? Y or N: ")
    if yesOrNo == "Y":
        createProject()
    elif yesOrNo == "N":
        return 0
    else:
        print("Oops... Something went wrong. Please re-run the script.")


    # install packages??
    print("\nPackages can be installed at any time by running pipenv in the directory " + project_folder + ".\n")
    yesOrNo = askUser("Install any packages right now? Y or N: ")

    if yesOrNo == "Y":
        installPackages()
    elif yesOrNo == "N":
        return 0
    else:
        print("Oops... Something went wrong. Please re-run the script.")

    print("Congratulations, your project is created!"
    print("Project path: " + project_folder + "\nVirtual environment path: " + venv_path")


main()
