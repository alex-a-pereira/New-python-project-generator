Author:

    Alex Pereira
    Alex--pereira@outlook.com
    https://github.com/alex-pereira

Project's purpose:

    This script is designed to automate the process of create a python project and virtual environment using pipenv.
    This is designed for use on windows only.

Install / Run:

    Clone, open command line, navigate to the directory that you clone the repo into, and run main.py as follows:

    *navigate to where you'd like to keep this script via file explorer, right click, and press "git bash here"

    git clone https://github.com/alex-pereira/New-python-project-generator.git

    *open command line

    cd ***PATH\THAT\YOU\CLONED\REPO***
    python main.py

Usage:

    First, when prompted, indicate with "Y" that you'd like to delete the directory credentials do so.
    Copy and paste the paths from file explorer winder to where you keep your python projects and where
    your .virtualenvs folder is located - usually under C:\users\*your_username*\.virtualenvs

    Then, specify with Y that you'd like to create a project. Type the desired project name when prompted.

    After the virtualenv is create, indicate whether or not you'd like to install any packages for this project.
    Packages can be installed normally at any time after the project is created. This is just for convenience.
    If you'd like to install any packages, type them in the following format:
        package1, package2, package3

Known issues:

    I suck at coding

Future plans:

    Integrate multi-os functionality using os.path rather than ntpath

    Integrate git functionality so the following will be automatically generated:
    1. an initilized .git directory
    2. a .gitignore specific to python
    3. a README.md