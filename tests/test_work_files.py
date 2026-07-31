import json
import pytest
from unittest.mock import patch, mock_open, Mock

from src.work_files import EditingFiles

from unittest.mock import patch, mock_open



def test_save_planes_list_objects_json(list_obj):

    mock_file = mock_open()

    with patch('src.work_files.open', mock_file):
        result = EditingFiles.save_planes_list_objects_json(list_obj)

    assert result is None
    mock_file.assert_called_once()
    mock_file().write.assert_called()


def test_delete_all_planes_list_objects_json():

    mock_file = mock_open()

    with patch('src.work_files.open', mock_file):
        result = EditingFiles.delete_all_planes_list_objects_json()

    assert result is None
    mock_file.assert_called_once()
    mock_file().write.assert_called()