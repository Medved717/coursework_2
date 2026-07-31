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
    def save_planes_list_objects_json(list_objects):
        """Перевод списка экземпляров класса (самолетов) в словарь и формирование списка словарей,
        после чего данные сохраняются в формате json."""

        data = [plane.to_dict() for plane in list_objects]

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, "data", "list_objects_planes.json")

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return None

    @staticmethod
    def delete_all_planes_list_objects_json():
        """Удаление всего списка самолетов в файле list_objects_planes.json"""

        current_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_file, "data", "list_objects_planes.json")

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)
        return None
