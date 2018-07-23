import os
import shutil


def create_project(project_name, project_directory, venv_directory, remote_url=""):
    path_list = [project_directory, venv_directory]
    writing_step(path_list)

    new_folder = os.path.join(project_directory, project_name)
    if not os.path.isdir(new_folder):
        os.mkdir(new_folder)

    run_pipenv(new_folder)
    copy_assets(new_folder)
    print("Project Created Successfully!")


def get_dir_defaults():
    paths = read_from_file()

    if not validate_paths(paths):
        return paths


def read_from_file():
    with open("paths.txt", "r") as fp:
        paths = fp.read().splitlines()

    return paths


def write_to_file(lines_to_write):
    with open("paths.txt", "w") as fp:
        fp.writelines("%s\n" % path for path in lines_to_write)


def writing_step(path_list):
    validation = validate_paths(path_list)

    if validation:  # if either path is invalid, return an error
        return 101
    if compare_paths(path_list):  # if either path doesn't match the file, re-write the file
        write_to_file(path_list)


def validate_paths(path_list):
    invalid_paths = []

    for idx, path in enumerate(path_list):
        if not os.path.isdir(path):
            invalid_paths.append(idx)

    if not invalid_paths:
        return 0
    else:
        return invalid_paths


def compare_paths(from_gui):
    from_file = read_from_file()

    diff = [i for i, j in zip(from_file, from_gui) if i != j]

    if not diff:
        return 0
    else:
        return 1





def run_pipenv(project_folder):
    os.environ["PIPENV_IGNORE_VIRTUALENVS"] = "1"

    owd = os.path.abspath(os.getcwd())

    os.chdir(project_folder)  # change the working directory
    os.system(project_folder[:2] + " & cd " + project_folder + " & pipenv --python 3.6")

    os.chdir(owd)


def copy_assets(project_folder):
    owd = os.path.abspath(os.getcwd())
    assets_folder = os.path.join(owd, "assets")

    files_to_copy = os.listdir(assets_folder)

    for file in files_to_copy:
        asset_path = os.path.join(assets_folder, file)
        shutil.copy(asset_path, project_folder)





