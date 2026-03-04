import unittest
from unittest.mock import MagicMock, patch
from atelier1_fmgr import FileManager


class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.file_selector = MagicMock()
        self.ui = MagicMock()
        self.file_manager = FileManager(
            file_selector=self.file_selector,
            ui=self.ui
        )

    @patch("atelier1_fmgr.shutil.copy2")
    def test_copy_files_success(self, mock_copy):
        self.file_selector.get_selected_files.return_value = ["/fake/file.txt"]

        self.file_manager.copy_files("/dest")

        mock_copy.assert_called_once_with("/fake/file.txt", "/dest")

    @patch("atelier1_fmgr.shutil.copy2", side_effect=Exception("Erreur copie"))
    def test_copy_files_ignore_once(self, mock_copy):
        self.file_selector.get_selected_files.return_value = [
            "/fake/file1.txt",
            "/fake/file2.txt"
        ]
        self.ui.error_choice.return_value = 0

        self.file_manager.copy_files("/dest")

        self.assertEqual(mock_copy.call_count, 2)

    @patch("atelier1_fmgr.shutil.copy2", side_effect=Exception("Erreur copie"))
    def test_copy_files_ignore_always(self, mock_copy):
        self.file_selector.get_selected_files.return_value = [
            "/fake/file1.txt",
            "/fake/file2.txt"
        ]
        self.ui.error_choice.return_value = 1

        self.file_manager.copy_files("/dest")

        self.assertEqual(mock_copy.call_count, 2)

    @patch("atelier1_fmgr.shutil.copy2", side_effect=Exception("Erreur copie"))
    def test_copy_files_stop(self, mock_copy):
        self.file_selector.get_selected_files.return_value = [
            "/fake/file1.txt",
            "/fake/file2.txt"
        ]
        self.ui.error_choice.return_value = 2

        self.file_manager.copy_files("/dest")

        self.assertEqual(mock_copy.call_count, 1)

 
    @patch("atelier1_fmgr.shutil.move")
    def test_move_files_success(self, mock_move):
        self.file_selector.get_selected_files.return_value = ["/fake/file.txt"]

        self.file_manager.move_files("/dest")

        mock_move.assert_called_once_with("/fake/file.txt", "/dest")


    @patch("atelier1_fmgr.os.remove")
    @patch("atelier1_fmgr.os.path.isfile", return_value=True)
    def test_delete_files_file(self, mock_isfile, mock_remove):
        self.file_selector.get_selected_files.return_value = ["/fake/file.txt"]

        self.file_manager.delete_files()

        mock_remove.assert_called_once_with("/fake/file.txt")

    @patch("atelier1_fmgr.shutil.rmtree")
    @patch("atelier1_fmgr.os.path.isdir", return_value=True)
    def test_delete_files_directory(self, mock_isdir, mock_rmtree):
        self.file_selector.get_selected_files.return_value = ["/fake/folder"]

        self.file_manager.delete_files()

        mock_rmtree.assert_called_once_with("/fake/folder")


if __name__ == "__main__":
    unittest.main()