import os
import shutil

class FileManager:
    def __init__(self, file_selector):
        self.file_selector = file_selector

    def copy_files(self, destination):
        for file in self.file_selector.get_selected_files():
            shutil.copy(file, destination)

    def move_files(self, destination):
        for file in self.file_selector.get_selected_files():
            shutil.move(file, destination)

    def delete_files(self):
        for file in self.file_selector.get_selected_files():
            os.remove(file)