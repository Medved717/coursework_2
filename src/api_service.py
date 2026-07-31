import requests
from abc import ABC, abstractmethod


class ApiService(ABC):

    @abstractmethod
    def get_aeroplanes(self, country: str) -> None:
        pass


class APIAdapter(ApiService):

    def __init__(self) -> None:
        self.openstreetmap_url = "https://nominatim.openstreetmap.org/search"
        self.opensky_url = "https://opensky-network.org/api/states/all?"
        self.aeroplanes = None

    def get_aeroplanes(self, country: str) -> None:
        """Собираем данные по стране, получаем координаты и в данном диапазоне получаем список самолетов."""
        headers_nominatim = {
            "User-Agent": "test-app/1.0",
        }

        # Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            "country": country,
            "format": "json",
            "limit": 1,
        }

        try:
            response = requests.get(
                url=self.openstreetmap_url,
                params=params_nominatim,
                headers=headers_nominatim,
                timeout=60,
            )
            response.raise_for_status()
        except Exception as a:
            print(
                f"Произошла ошибка получения данных от источника - nominatim\nКод ошибки: {a}"
            )
            return None

        data = response.json()

        if not data:
            print("Страна не найдена в базе Nominatim")
            return None

        if "boundingbox" not in data[0]:
            print("В ответе отсутствуют координаты boundingbox.")
            return None

        geo_coordinates = data[0].get("boundingbox")

        if not geo_coordinates or len(geo_coordinates) != 4:
            print("Ошибка! Отсутствуют координаты или получен их неполный список.")
            return None

        # Параметры для фильтрации самолетов по их географическим координатам.
        params = {
            "lamin": float(geo_coordinates[0]),
            "lamax": float(geo_coordinates[1]),
            "lomin": float(geo_coordinates[2]),
            "lomax": float(geo_coordinates[3]),
        }

        try:
            response = requests.get(url=self.opensky_url, params=params, timeout=60)
            response.raise_for_status()
        except Exception as e:
            print(
                f"Произошла ошибка получения данных от источника - opensky\nКод ошибки: {e}"
            )
            return None

        # Это результат программы в формате словаря
        self.aeroplanes = response.json()
        return self
