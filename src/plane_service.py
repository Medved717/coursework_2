import os
import json


class Aeroplane:
    country_of_registration: str
    call_sign: str
    velocity: float
    geo_altitude: float


    def __init__(self, country_of_registration, call_sign, velocity , geo_altitude):
        self. country_of_registration = country_of_registration
        self.call_sign = call_sign
        self.velocity = velocity
        self.geo_altitude = geo_altitude


    # @staticmethod
    # def cast_to_object_list(dict_planes):
    #     """Создаем список объектов (самолетов) из полученных сведений API."""
    #
    #     list_planes = dict_planes.get("states", [])
    #
    #     new_list_plane = []
    #
    #     for i in list_planes:
    #         new_plane = Aeroplane.get_plane(i)
    #         new_list_plane.append(new_plane)
    #
    #     return new_list_plane

    @classmethod
    def get_plane_obj(cls, planes):
        "Создаем экземпляры класса (Самолеты) по следующим параметрам с обязательной валидацией."

        list_obj = []
        for plane in planes["states"]:
            list_obj.append(cls(country_of_registration=plane[2].strip() if plane[2] else 'Неизвестно',
                             call_sign=plane[1].strip() if plane[1] else 'Неизвестно',
                             velocity=plane[9] if plane[9] is not None else 0.0,
                             geo_altitude=plane[13] if plane[13] is not None else 0.0))
        return list_obj

    def __repr__(self):
        return f'Aeroplane("{self.country_of_registration}", "{self.call_sign}", {self.velocity}, {self.geo_altitude})'


    def height_comparison(self, other):
        """Сравнение самолетов по высоте полета."""

        if self.geo_altitude > other.geo_altitude:
            return self
        else:
            return other

    def speed_comparison(self, other):
        """Сравнение самолетов по скорости полета."""

        return self if self.velocity > other.velocity else other

    @staticmethod
    def speed_filter(data, speeds):
        """Фильтр самолетов по скорости полета."""

        min_speed, max_speed = speeds[0].strip(), speeds[1].strip()
        list_planes_obj = [plane for plane in data if float(min_speed) <= plane.velocity <= float(max_speed)]
        sorted_list = sorted(list_planes_obj, key=lambda x: x.velocity, reverse=True)
        return sorted_list

    def top_geo_altitude(data, top):
        """Получение топ самолетов по высоте."""

        list_dict_panes = sorted(data, key=lambda x: x.geo_altitude, reverse=True)

        if len(list_dict_panes) < int(top):
            print('Список самолетов меньше указанного топа.')
            return list_dict_panes
        else:
            return list_dict_panes[:top]

    def to_dict(self):
        """Перевод объекта класса в словарь."""

        return {'country_of_registration':self.country_of_registration,
                'call_sign': self.call_sign,
                'velocity': self.velocity,
                'geo_altitude':self.geo_altitude}

    def search_plane_call_sing(data, call_sign):
        """Ищем самолеты по позывному и выводим списки найденных объектов"""

        sorted_call_sing = [plain for plain in data if plain.call_sign == call_sign]
        return sorted_call_sing

    @staticmethod
    def search_plane_country_of_registration(data, country_of_registration):
        """Ищем самолеты по странам и выводим списки."""

        list_country = [plain for plain in data if plain.country_of_registration == country_of_registration]
        return list_country