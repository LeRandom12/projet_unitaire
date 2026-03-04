import os

class FileSelector:
    def __init__(self):
        self.selected_files = []
        self.current_directory_contents = []

    def load_directory_contents(self, directory_path):
        self.current_directory_contents = os.listdir(directory_path)

    def select_files_by_indices(self, indices, directory_path):
        self.selected_files = [
            os.path.join(directory_path, self.current_directory_contents[i])
            for i in indices
        ]

    def get_selected_files(self):
        return self.selected_files

    def clear_selection(self):
        self.selected_files = []