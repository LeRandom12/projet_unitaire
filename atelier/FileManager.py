class FileManager:
    def __init__(self, file_selector, filesystem):
        self.file_selector = file_selector
        self.filesystem = filesystem

    def copy_files(self, destination):
        for file in self.file_selector.get_selected_files():
            self.filesystem.copy(file, destination)

    def move_files(self, destination):
        for file in self.file_selector.get_selected_files():
            self.filesystem.move(file, destination)

    def delete_files(self):
        for file in self.file_selector.get_selected_files():
            self.filesystem.delete(file)