import requests
from src.api_service import APIAdapter
from src.plane_service import Aeroplane
from src.work_files import EditingFiles


def user_interaction():
    """Функция для взаимодействия с пользователем."""

    # Получаем список самолетов переводим их в список словарей и сохраняем в формате json.
    country = input("Введите название страны: ")
    api = APIAdapter()
    api.get_aeroplanes(str(country))

    # Создаем список экземпляров классов
    get_aeroplanes_country_obj = Aeroplane.get_plane_obj(api.aeroplanes)

    # Для сохранения данных в формате json переводим объекты в словарь и сохраняем.
    EditingFiles.save_planes_list_objects_json(get_aeroplanes_country_obj)
    print(f'Данные со списком самолетов введенной странны ({country}) получены и\n '
          f'сохранены в файл: save_api_info_json.txt.')

    # Проводим фильтрацию списка по стране регистрации.
    country = input("Введите название страны для фильтрации по стране регистрации: ")
    country_filter = Aeroplane.search_plane_country_of_registration(get_aeroplanes_country_obj, country)














    # Предлагаем ввести диапозон скорости для поиска и фильтрации по заданным параметрам.
    #
    # Aeroplane.speed_filter(get_aeroplanes_country_obj, min_speed, max_speed)







    # top_n = int(input("Введите количество самолетов для вывода в топ N по высоте: "))
    # altitude_range = input("Введите диапазон высот полета: ") # Пример: 100000 - 150000








if __name__ == "__main__":
    user_interaction()

# Canada