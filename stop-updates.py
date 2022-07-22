import os
import re
from datetime import datetime as dt


class ManifestFile:

    def __init__(self, install_dir, app_id):
        """Find the path for manifest file of app_id in install_dir."""
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

        self.dir = install_dir
        self.name = file_name
        self.full_path = f"{install_dir}{file_name}"

        self.create_backup()

    def create_backup(self):
        """Create backup of the manifest file."""
        try:
            with open(self.full_path, mode="r") as file:
                file_contents = file.read()
            file.close()

            name_list = self.name.split('.')
            if len(name_list) > 2:
                raise ValueError("Manifest file contains unexpected number of . characters.")
            now = dt.now()
            backup_name = f"{name_list[0]}_BACKUP{now.strftime('%m%d%Y%H%M%S')}.{name_list[1]}"

            backup_path = f"{self.dir}{backup_name}"
            print(f"Generating backup file: {backup_path}")

            try:
                with open(backup_path, mode="w") as backup_file:
                    backup_file.write(file_contents)
                backup_file.close()

            except Exception as E:
                raise Exception

            else:
                print("Backup file generation successful!")

        except ValueError as E:
            raise ValueError(E)


def main():
    path = "C:\\Program Files (x86)\\Steam\\steamapps\\"
    app_id = "620980"
    # Constants be replaced by user input later

    ManifestFile(path, app_id)
    print("Enjoy playing your game without updating :)")


if __name__ == '__main__':
    main()
