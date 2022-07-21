import os
import re


def get_manifest_file(install_dir, app_id):
    """Return JSON file of app_id's manifest from within install_dir."""
    file_list = list(os.scandir(install_dir))
    pattern = rf"appmanifest_{app_id}\.acf"
    try:
        matches = [x.name for x in file_list if re.search(pattern, x.name)]

        if len(matches) == 0:
            raise ValueError(f"No results for app_id {app_id} in directory {install_dir}.")
        elif len(matches) > 1:
            raise ValueError(f">1 result for app_id {app_id} in directory {install_dir}.")
        else:
            file_name = matches[0]

    except ValueError as E:
        raise ValueError(E)

    full_path = f"{install_dir}{file_name}"
    print(f"Found manifest file: {full_path}")

    with open(full_path, mode="r") as file:
        data = file.read()

    print(data)


def main():
    path = "C:\\Program Files (x86)\\Steam\\steamapps\\"
    app_id = "620980"
    get_manifest_file(path, app_id)
    print("Enjoy playing your game without updating :)")


if __name__ == '__main__':
    main()
