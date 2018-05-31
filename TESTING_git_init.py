def gitInit():
    yesOrNo = askUser("Initialize a git repo? Y or N: ")

    if yesOrNo == "Y":
        repo_dir = project_folder
        r = git.Repo.init(repo_dir)
        r.index.add()

    elif yesOrNo == "N":
        return 0
    else:
        print("Oops... Something went wrong. Please re-run the script.")