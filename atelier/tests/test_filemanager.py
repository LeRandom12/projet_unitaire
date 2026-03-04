import unittest
from unittest.mock import MagicMock, patch

from atelier1_fmgr import FileManager


class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.file_manager = FileManager()
        self.file_manager.file_selector = MagicMock()

    @patch("atelier1_fmgr.shutil.copy2")
    @patch("atelier1_fmgr.os.path.exists")
    def test_copy_files(self, mock_exists, mock_copy):
        mock_exists.return_value = True
        self.file_manager.file_selector.get_selected_files.return_value = [
            "/fake/file1.txt",
            "/fake/file2.txt"
        ]

        self.file_manager.copy_files("/fake/destination")

        self.assertEqual(mock_copy.call_count, 2)
        self.file_manager.file_selector.clear_selection.assert_called_once()

    @patch("atelier1_fmgr.shutil.move")
    @patch("atelier1_fmgr.os.path.exists")
    def test_move_files(self, mock_exists, mock_move):
        mock_exists.return_value = True
        self.file_manager.file_selector.get_selected_files.return_value = [
            "/fake/file.txt"
        ]

        self.file_manager.move_files("/fake/destination")

        mock_move.assert_called_once_with("/fake/file.txt", "/fake/destination")
        self.file_manager.file_selector.clear_selection.assert_called_once()

    @patch("atelier1_fmgr.os.remove")
    @patch("atelier1_fmgr.os.path.isfile")
    def test_delete_files_file(self, mock_isfile, mock_remove):
        mock_isfile.return_value = True
        self.file_manager.file_selector.get_selected_files.return_value = [
            "/fake/file.txt"
        ]

        self.file_manager.delete_files()

        mock_remove.assert_called_once_with("/fake/file.txt")
        self.file_manager.file_selector.clear_selection.assert_called_once()

    @patch("atelier1_fmgr.shutil.rmtree")
    @patch("atelier1_fmgr.os.path.isdir")
    def test_delete_files_directory(self, mock_isdir, mock_rmtree):
        mock_isdir.return_value = True
        self.file_manager.file_selector.get_selected_files.return_value = [
            "/fake/folder"
        ]

        self.file_manager.delete_files()

        mock_rmtree.assert_called_once_with("/fake/folder")
        self.file_manager.file_selector.clear_selection.assert_called_once()


if __name__ == "__main__":
    unittest.main()