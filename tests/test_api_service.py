from unittest.mock import Mock, patch
from src.api_service import APIAdapter


# Рассуждения для плохо усвоенного Mock()
# Создаю патч, что мокаем requsets.get в данном модуле.
@patch("src.api_service.requests.get")
def test_get_aeroplanes(mock_get):  # В переменную внес мок, который глушит requsets.get

    # Создаю заглушку для ответа на запрос mock_get (requests.get) для сайта с картами.
    mock_response_map = Mock()

    # Не понимаю, почему что тут будет происходить?  Получается,
    # что людое использование json будет выводить это?
    mock_response_map.json.return_value = [
        {"boundingbox": ["48.0", "49.0", "2.0", "3.0"]}
    ]

    # Создаю заглушку для ответа на запрос mock_get (requests.get) для сайта с самолетами.
    mock_response_plane = Mock()

    # Не понимаю, почему что тут будет происходить?  Получается,
    # что людое использование json будет выводить это?
    mock_response_plane.json.return_value = {
        "time": 1785476770,
        "states": [
            [
                "39de4f",
                "TVF6306 ",
                "France",
                1785476769,
                1785476769,
                2.3485,
                47.9893,
                6598.92,
                False,
                203.59,
                164.31,
                11.7,
                None,
                6941.82,
                "7635",
                False,
                0,
            ]
        ],
    }

    # Здесь создаем ситуацию с помощью метода side_effect по которому будет распределены возвращения
    # mock_get в каждом из разов, т.е. в первый вызов вернется mock_response_map, а во второй mock_response_plane
    mock_get.side_effect = [mock_response_map, mock_response_plane]

    api = APIAdapter()
    api.get_aeroplanes("France")
    assert api.aeroplanes["states"][0][2] == "France"
