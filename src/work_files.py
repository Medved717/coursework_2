from abc import ABC, abstractmethod
import os
import json
from idlelib.iomenu import encoding

from src.api_service import APIAdapter
from src.plane_service import Aeroplane


class WorkFiles(ABC):

    @abstractmethod
    def save_planes_json(self, data):
        pass

    @abstractmethod
    def save_planes_list_objects_json(self, list_objects):
        pass

    @abstractmethod
    def delete_all_planes_list_objects_json(self):
        pass

class EditingFiles(WorkFiles):

    def save_planes_json(self, data):
        """Сохраняем результаты полученные по API соединению в сыром виде."""

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, 'data', 'save_api_info_json.txt')

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return self


    def save_planes_list_objects_json(self, list_objects):
        """Перевод списка экземпляров класса (самолетов) в словарь и формирование списка словарей,
        после чего данные сохраняются в формате json."""

        data = [plane.to_dict() for plane in list_objects]

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, 'data', 'list_objects_planes.json')

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


    def delete_all_planes_list_objects_json(self):
        """Удаление всего списка самолетов в файле list_objects_planes.json"""

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, 'data', 'list_objects_planes.json')

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([], f)

    def search_plane_call_sing(call_sign):

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