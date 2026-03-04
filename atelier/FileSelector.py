import os

class FileSelector:
    def __init__(self):
        self.selected_files = []
        self.current_directory_contents = []

    def load_directory_contents(self, directory_path):
        try:
            self.current_directory_contents = os.listdir(directory_path)
            return self.current_directory_contents
        except Exception:
            return []

    def select_files_by_indices(self, indices, directory_path):
        self.selected_files.clear()
        selected_indices = [int(i.strip()) for i in indices.split(',')]

        for index in selected_indices:
            if 0 <= index < len(self.current_directory_contents):
                full_path = os.path.join(directory_path, self.current_directory_contents[index])
                self.selected_files.append(full_path)

        return self.selected_files

    def get_selected_files(self):
        return self.selected_files

    def clear_selection(self):
        self.selected_files.clear()