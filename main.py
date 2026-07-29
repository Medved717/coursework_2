# import requests
# # Создание экземпляра класса для работы с API сайтов с самолетами
# api = AeroplanesAPI()
#
# # Получение информации о самолетах с opensky-network.org
# aeroplanes = api.get_aeroplanes(‘Spain’)
#
# # Преобразование набора данных в список объектов
# aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)
#
# # Пример работы контструктора класса с одним самолетом
# aeroplane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)
#
# # Сохранение информации в файл
# json_saver = JSONSaver()
# json_saver.add_aeroplane(vacancy)
# json_saver.delete_aeroplane(vacancy)
#
# # Функция для взаимодействия с пользователем
# def user_interaction():
#     country = input("Введите название страны: ")
#     top_n = int(input("Введите количество самолетов для вывода в топ N: "))
#     filter_words = input("Введите названия стран для фильтрации по стране регистрации: ").split()
#     altitude_range = input("Введите диапазон высот полета: ") # Пример: 100000 - 150000
#
#     filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)
#
#     ranged_aeroplanes = get_aeroplanes_by_altitude(aeroplanes, altitude_range)
#
#     sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
#     top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
#     print_aeroplanes(top_aeroplanes)
#
#
# if __name__ == "__main__":
#     user_interaction()




import json
from xml.etree.ElementTree import indent

from src.api_service import APIAdapter
from src.plane_service import Aeroplane
from src.work_files import EditingFiles, WorkFiles
import os


# # Проверка записи сырого файла в файл в формате json.
# if __name__ == "__main__":
#
#     file_result = os.path.join('data', 'save_api_info_json.txt')
#     with open(file_result, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#
#     result = Aeroplane.cast_to_object_list(data)
#     for i in result:
#         print(i)
#
#
# # Проверка методов сравнения.
# if __name__ == "__main__":
#
#     plane_1 = Aeroplane('Canada', 'WJA221', 178.08, 12694.92)
#     plane_2 = Aeroplane('Canada', 'ROU1922', 288.85, 11117.58)
#     result_1 = plane_1.height_comparison(plane_2)
#     result_2 = plane_2.speed_comparison(plane_1)
#     print(result_1)
#     print(result_2)
#
#
# # Проверка записи готового файла со всем списком самолетов в файл в формате json.
# if __name__ == "__main__":
#
#     api = APIAdapter()
#     api.get_aeroplanes('Russia')
#     list_planes = Aeroplane.cast_to_object_list(api.aeroplanes)
#     EditingFiles.save_planes_list_objects_json(list_planes)


# # Проверка поиска самолетов по-позывному и стране.
# if __name__ == "__main__":
#     result = EditingFiles.search_plane_call_sing("VJA535")
#     result_2 = EditingFiles.search_plane_country_of_registration("Canada")
#     print(result)
#     for i in result_2:
#         print(i)



# Проверка поиска самолетов по-позывному и стране.
if __name__ == "__main__":
    sorted_file = Aeroplane.top_geo_altitude(200)

    for i in sorted_file:
        print(i)