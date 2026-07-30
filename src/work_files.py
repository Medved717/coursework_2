from abc import ABC, abstractmethod
import os
import json
from src.plane_service import Aeroplane


class WorkFiles(ABC):

    @staticmethod
    @abstractmethod
    def save_planes_json(data):
        pass

    @staticmethod
    @abstractmethod
    def save_planes_list_objects_json(list_objects):
        pass

    @staticmethod
    @abstractmethod
    def delete_all_planes_list_objects_json():
        pass


class EditingFiles(WorkFiles):

    @staticmethod
    def save_planes_txt(data):
        """Сохраняем результаты полученные по API соединению в сыром виде."""

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, 'data', 'save_api_info_json.txt')

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return None

    @staticmethod
    def save_planes_list_objects_json(list_objects):
        """Перевод списка экземпляров класса (самолетов) в словарь и формирование списка словарей,
        после чего данные сохраняются в формате json."""

        data = [plane.to_dict() for plane in list_objects]

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, 'data', 'list_objects_planes.json')

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return None

    @staticmethod
    def delete_all_planes_list_objects_json():
        """Удаление всего списка самолетов в файле list_objects_planes.json"""

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, 'data', 'list_objects_planes.json')

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([], f)
        return None

    def speed_filter_file(min_speed, max_speed):
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

    def search_plane_country_of_registration_file(country_of_registration):
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

    def search_plane_call_sing_files(call_sign):
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

        def to_obj(dict_obj):
            """Перевод из словаря в объект класса Aeroplane."""

            return Aeroplane(dict_obj['country_of_registration'],
                             dict_obj['call_sign'],
                             dict_obj['velocity'],
                             dict_obj['geo_altitude'])