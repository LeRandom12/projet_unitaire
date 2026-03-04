import os
import shutil
from user_interface import UserInterface


class FileManager:
    def __init__(self, file_selector=None, ui=None):
        self.file_selector = file_selector
        self.ui = ui or UserInterface()
        self.ignore_all_errors = False

    def copy_files(self, destination):
        selected_files = self.file_selector.get_selected_files()

        for file in selected_files:
            try:
                shutil.copy2(file, destination)
            except Exception as e:
                if self.ignore_all_errors:
                    continue

                choice = self.ui.error_choice(str(e))

                if choice == 0:
                    continue
                elif choice == 1:
                    self.ignore_all_errors = True
                    continue
                elif choice == 2:
                    break

        self.file_selector.clear_selection()

    def move_files(self, destination):
        selected_files = self.file_selector.get_selected_files()

        for file in selected_files:
            try:
                shutil.move(file, destination)
            except Exception as e:
                choice = self.ui.error_choice(str(e))
                if choice == 2:
                    break

        self.file_selector.clear_selection()

    def delete_files(self):
        selected_files = self.file_selector.get_selected_files()

        for path in selected_files:
            try:
                if os.path.isfile(path):
                    os.remove(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path)
            except Exception as e:
                choice = self.ui.error_choice(str(e))
                if choice == 2:
                    break

        self.file_selector.clear_selection()