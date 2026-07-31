import pytest
from src.plane_service import Aeroplane


def test_get_plane_obj(raw_information_1):

    result = Aeroplane.get_plane_obj(raw_information_1)
    assert str(result[0]) == str(Aeroplane('France', 'TVF6306',
                                           203.59, 6941.82))

def test_speed_filter(list_obj, list_obj_sorted_speed):

    speeds = ['100', '300']
    result = Aeroplane.speed_filter(list_obj, speeds)
    assert len(result) == 9


@pytest.mark.parametrize('obj, expected_dict', [
    (Aeroplane("Russia", "AFR511", 262.96, 12915.9),
     {'country_of_registration': 'Russia', 'call_sign': 'AFR511', 'velocity': 262.96, 'geo_altitude': 12915.9}),
    (Aeroplane("Oman", "AFR705", 252.31, 12915.9),
     {'country_of_registration': 'Oman', 'call_sign': 'AFR705', 'velocity': 252.31, 'geo_altitude': 12915.9}),
    (Aeroplane("Russia", "AFR75K", 280.22, 12832.08),
     {'country_of_registration': 'Russia', 'call_sign': 'AFR75K', 'velocity': 280.22, 'geo_altitude': 12832.08})
                                      ]
                         )
def test_to_dict(obj, expected_dict):

    assert Aeroplane.to_dict(obj) == expected_dict


def test_top_geo_altitude(list_obj, list_obj_sorted_geo):
    result = Aeroplane.top_geo_altitude(list_obj, 10)
    assert result[0].country_of_registration == "Oman"
