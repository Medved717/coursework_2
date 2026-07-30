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

    @staticmethod
    def cast_to_object_list(dict_planes):
        """Создаем список объектов (самолетов) из полученных сведений API."""

        list_planes = dict_planes.get("states", [])

        new_list_plane = []

        for i in list_planes:
            new_plane = Aeroplane.get_plane(i)
            new_list_plane.append(new_plane)

        return new_list_plane

    @classmethod
    def get_plane(cls, plane):
        "Создаем экземпляры класса (Самолеты) по следующим параметрам с обязательной валидацией."

        return cls(country_of_registration=plane[2].strip() if plane[2] else 'Неизвестно',
                         call_sign=plane[1].strip() if plane[1] else 'Неизвестно',
                         velocity=plane[9] if plane[9] is not None else 0.0,
                         geo_altitude=plane[13] if plane[13] is not None else 0.0)

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

    def speed_filter(min_speed, max_speed):
        """Фильтр самолетов по скорости полета."""

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, 'data', 'list_objects_planes.json')

        with open(file_path, 'r', encoding='utf-8') as f:
            data_planes = json.load(f)

        list_planes_dict = [plane for plane in data_planes if min_speed <= plane['velocity'] <= max_speed]
        sorted_list = sorted(list_planes_dict, key=lambda x: x['velocity'], reverse=True)
        list_planes = []
        for plane in sorted_list:
            plane_obj = Aeroplane.to_obj(plane)
            list_planes.append(plane_obj)

        return list_planes

    def top_geo_altitude(top):
        """Получение топ самолетов по высоте."""

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, 'data', 'list_objects_planes.json')

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        list_obj = []
        list_dict_panes = sorted(data, key=lambda x: x['geo_altitude'], reverse=True)
        for plane in list_dict_panes:
            obj = Aeroplane.to_obj(plane)
            list_obj.append(obj)

        if len(list_obj) < int(top):
            print('Список самолетов меньше указанного топа.')
            return list_obj
        else:
            return list_obj[:top]

    def to_dict(self):
        """Перевод объекта класса в словарь."""

        return {'country_of_registration':self.country_of_registration,
                'call_sign': self.call_sign,
                'velocity': self.velocity,
                'geo_altitude':self.geo_altitude}

    def to_obj(dict_obj):
        """Перевод из словаря в объект класса Aeroplane."""

        return Aeroplane(dict_obj['country_of_registration'],
                dict_obj['call_sign'],
                dict_obj['velocity'],
                         dict_obj['geo_altitude'])

    def search_plane_call_sing(call_sign):
        """Ищем самолеты по позывному и выводим списки найденных объектов"""

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, 'data', 'list_objects_planes.json')

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        list_search_obg_plane = []
        sorted_call_sing = [plain for plain in data if plain['call_sign'] == call_sign]
        for plane in sorted_call_sing:
            obj_plane = Aeroplane.to_obj(plane)
            list_search_obg_plane.append(obj_plane)
        return list_search_obg_plane

    def search_plane_country_of_registration(country_of_registration):
        """Ищем самолеты по странам и выводим списки."""

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, 'data', 'list_objects_planes.json')

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        list_search_obg_plane_country = []
        sorted_call_sing = [plain for plain in data if plain['country_of_registration'] == country_of_registration]
        for plane in sorted_call_sing:
            obj_plane = Aeroplane.to_obj(plane)
            list_search_obg_plane_country.append(obj_plane)
        return list_search_obg_plane_country