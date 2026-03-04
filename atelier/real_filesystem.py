
import os
import shutil
from filesystem_interface import FileSystemInterface

class RealFileSystem(FileSystemInterface):
    def copy(self, src, dst):
        shutil.copy(src, dst)

    def move(self, src, dst):
        shutil.move(src, dst)

    def delete(self, path):
        os.remove(path)