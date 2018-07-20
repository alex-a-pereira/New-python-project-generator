import os

def check_textfile(project_dir, venv_dir):
    with open("paths.txt", "r") as fp:
        paths = fp.read().splitlines()

        if paths[0] != project_dir or paths[1] != venv_dir:
            fp = open("paths.txt", "r")
            fp.writelines([project_dir, venv_dir])


def validate(project_dir, venv_dir):
    if not os.path.isdir(project_dir):
        return "Error - Project path does not exist"
    elif not os.path.isdir(venv_dir):
        return "Error - Virtual Environment path does not exist"
    else:
        return 0


def create(project_name, project_directory, venv_directory, remote_url=""):
    project_path = os.path.abspath(project_directory)
    venv_path = os.path.abspath(venv_directory)

    paths_status = validate(project_directory, venv_directory)
    if paths_status != 0:
        return paths_status

    check_textfile(project_path, venv_directory)

    project_dir = os.path.join(project_path, project_name)
    if not os.path.isdir(project_dir):
        os.mkdir(project_dir)

    os.environ["PIPENV_IGNORE_VIRTUALENVS"] = "1"
    os.chdir(project_dir)  # change the working directory
    os.system(project_dir[:2] + " & cd " + project_dir + " & pipenv --python 3.6")
