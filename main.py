import requests
from src.api_service import APIAdapter
from src.plane_service import Aeroplane
from src.work_files import EditingFiles

# # Создание экземпляра класса для работы с API сайтов с самолетами
# api = APIAdapter()
#
# # Получение информации о самолетах с opensky-network.org
# aeroplanes = api.get_aeroplanes('Spain')
#
# # Преобразование набора данных в список объектов
# aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)
# #
# # # Пример работы контструктора класса с одним самолетом
# # aeroplane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)
#
# # Сохранение информации в файл
# json_saver = EditingFiles.save_planes_json(aeroplanes)
# EditingFiles.save_planes_list_objects_json()
# EditingFiles.delete_all_planes_list_objects_json()
#
# # Функция для взаимодействия с пользователем
# def user_interaction():
#     country = input("Введите название страны: ")
#     filter_words = input("Введите названия стран для фильтрации по стране регистрации: ").split()
#     top_n = int(input("Введите количество самолетов для вывода в топ N по высоте: "))
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

result = Aeroplane.speed_filter(111, 200)
for i in result:
    print(i)