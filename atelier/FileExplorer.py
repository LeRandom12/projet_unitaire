import os

class FileExplorer:
    def __init__(self, start_path, file_selector):
        self.current_path = start_path
        self.file_selector = file_selector

    def display_directory_contents(self):
        files = os.listdir(self.current_path)
        self.file_selector.load_directory_contents(self.current_path)

        for i, file in enumerate(files):
            print(f"{i} - {file}")

    def navigate(self, index):
        files = os.listdir(self.current_path)
        new_path = os.path.join(self.current_path, files[index])

        if os.path.isdir(new_path):
            self.current_path = new_path
        else:
            print("Ce n'est pas un dossier")

    def go_to_parent_directory(self):
        self.current_path = os.path.dirname(self.current_path)