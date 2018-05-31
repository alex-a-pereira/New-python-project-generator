"""
Author & sole contributor:
Alex Pereira
Alex--pereira@outlook.com

To create a new project and venv on Windows I have to do the following:
1. create the directory for the project using the user-specified project_name
2. create a virtual environment with pipenv via command line
3. install packages to the virtual environment

"""
import os
import time
import shutil

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


def checkCredentials():

    global project_dir
    global venv_dir

    print("Initializing...\n")
    time.sleep(1)

    file_name = "secrets.txt"
    file = open(file_name, "r+")
    # try block to make sure that our secrets file exists, and if not it creates one
    try:
        f = file
    except FileNotFoundError:
        f = open(file_name, "w+")
        f.close()

    def writeFile():
        # open my file, and if it isn't composed of two lines
        with open(file_name, "r+") as file:
            if len(file.readlines()) != 5:
                file.truncate(0)
                file.write("Project directory:\n")
                file.write(input("Please specify project directory using forward slashes: ") + "\n\n")
                file.write("Virtual environment directory:\n")
                file.write(input("Please specify virtual environment directory using forward slashes: ") + "\n")
            else:
                print("Project and virtual environments already specified.\n")
    writeFile()

    print("\n***Ensure directory locations below are valid***")
    print(file.read())

    yesOrNo = askUser("Delete and re-enter credentials? Y or N: ")
    while yesOrNo == "Y":
        print("\nEnter directories again using forward slashes:")
        file.truncate(0)

        writeFile()

        print("")
        file = open(file_name, "r+")
        print(file.read())
        yesOrNo = askUser("Delete and re-enter credentials? Y or N: ")
    file = open(file_name, "r+")
    list = file.readlines()

    project_dir = list[1]
    project_dir = project_dir[:int(len(project_dir) - 1)]
    if project_dir[-1:] != "/":
        project_dir = project_dir + "/"

    venv_dir = list[4]
    venv_dir = venv_dir[:int(len(venv_dir) - 1)]
    if venv_dir[-1:] != "/":
        venv_dir = venv_dir + "/"


def createProject():

    yesOrNo = askUser("Create a project? Y or N: ")

    if yesOrNo == "Y":
        # global variables project_name and project_folder are re-assigned in this function
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
        # assign the variable project_folder to our new dir's path and create a venv
        project_folder = project_dir + project_name
        os.system(project_folder[:2] + " & cd " + project_folder + " & pipenv --python 3.6")

        # specify the project's virtual environment
        os.chdir(venv_dir)
        all_venvs = [d for d in os.listdir('.') if os.path.isdir(d)]
        project_venv = max(all_venvs, key=os.path.getmtime)
        venv_path = venv_dir + project_venv
        print("Project created.\nProject path: " + project_folder + "\nVirtual environment path: " + venv_path)

        os.chdir(project_folder)

    elif yesOrNo == "N":
        return 0
    else:
        print("Oops... Something went wrong. Please re-run the script.")


def installPackages():

    os.chdir(project_folder)

    print("\nPackages can be installed at any time by running pipenv in the directory " + project_folder + ".\n")
    yesOrNo = askUser("Install any packages right now? Y or N: ")

    if yesOrNo == "Y":
        while yesOrNo != "N":  # the loop should continue to run
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

    elif yesOrNo == "N":
        return 0
    else:
        print("Oops... Something went wrong. Please re-run the script.")


def main():
    checkCredentials()
    createProject()
    installPackages()


main()
