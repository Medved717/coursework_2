import pytest
from src.plane_service import Aeroplane


def test_get_plane_obj(raw_information_1):
    result = Aeroplane.get_plane_obj(raw_information_1)
    assert str(result[0]) == str(Aeroplane('France', 'TVF6306',
                                           203.59, 6941.82))

def test_speed_filter(list_obj_sorted_speed):
    speeds = ['100', '300']
    result = Aeroplane.speed_filter(list_obj_sorted_speed, speeds)
    assert result == list_obj_sorted_speed


