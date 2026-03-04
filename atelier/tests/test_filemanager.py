import unittest
from unittest.mock import MagicMock, patch
from atelier1_fmgr import FileManager


class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.file_manager = FileManager()
        self.file_manager.file_selector = MagicMock()

  
    @patch("atelier1_fmgr.shutil.copy2")
    @patch("atelier1_fmgr.os.path.exists")
    def test_copy_files_normal(self, mock_exists, mock_copy):
        mock_exists.return_value = True
        self.file_manager.file_selector.get_selected_files.return_value = [
            "/fake/file1.txt"
        ]

        self.file_manager.copy_files("/dest")

        mock_copy.assert_called_once()

    @patch("atelier1_fmgr.shutil.copy2")
    def test_copy_files_no_selection(self, mock_copy):
        self.file_manager.file_selector.get_selected_files.return_value = []

        self.file_manager.copy_files("/dest")

        mock_copy.assert_not_called()

    @patch("atelier1_fmgr.os.path.exists")
    @patch("atelier1_fmgr.shutil.copy2")
    def test_copy_files_file_not_exists(self, mock_copy, mock_exists):
        mock_exists.return_value = False
        self.file_manager.file_selector.get_selected_files.return_value = [
            "/fake/file.txt"
        ]

        self.file_manager.copy_files("/dest")

        mock_copy.assert_not_called()

    @patch("atelier1_fmgr.shutil.move")
    @patch("atelier1_fmgr.os.path.exists")
    def test_move_files_normal(self, mock_exists, mock_move):
        mock_exists.return_value = True
        self.file_manager.file_selector.get_selected_files.return_value = [
            "/fake/file.txt"
        ]

        self.file_manager.move_files("/dest")

        mock_move.assert_called_once()

    @patch("atelier1_fmgr.shutil.move")
    def test_move_files_no_selection(self, mock_move):
        self.file_manager.file_selector.get_selected_files.return_value = []

        self.file_manager.move_files("/dest")

        mock_move.assert_not_called()


    @patch("atelier1_fmgr.os.remove")
    @patch("atelier1_fmgr.os.path.isfile")
    def test_delete_files_file(self, mock_isfile, mock_remove):
        mock_isfile.return_value = True
        self.file_manager.file_selector.get_selected_files.return_value = [
            "/fake/file.txt"
        ]

        self.file_manager.delete_files()

        mock_remove.assert_called_once()

    @patch("atelier1_fmgr.shutil.rmtree")
    @patch("atelier1_fmgr.os.path.isdir")
    def test_delete_files_directory(self, mock_isdir, mock_rmtree):
        mock_isdir.return_value = True
        self.file_manager.file_selector.get_selected_files.return_value = [
            "/fake/folder"
        ]

        self.file_manager.delete_files()

        mock_rmtree.assert_called_once()

    def test_delete_files_no_selection(self):
        self.file_manager.file_selector.get_selected_files.return_value = []

        # Ne doit pas lever d'erreur
        self.file_manager.delete_files()