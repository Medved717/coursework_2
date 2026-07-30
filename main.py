import requests
from src.api_service import APIAdapter
from src.plane_service import Aeroplane
from src.work_files import EditingFiles


def user_interaction():
    """Функция для взаимодействия с пользователем."""

    # Получаем список самолетов переводим их в список словарей и сохраняем в формате json.
    country = input("Введите название страны, (например - Canada): ")
    api = APIAdapter()
    api.get_aeroplanes(str(country))

    # Создаем список экземпляров классов
    get_aeroplanes_country_obj = Aeroplane.get_plane_obj(api.aeroplanes)

    # Для сохранения данных в формате json переводим объекты в словарь и сохраняем.
    EditingFiles.save_planes_list_objects_json(get_aeroplanes_country_obj)
    print(f'Данные со списком самолетов введенной странны ({country}) получены и\n'
          f'сохранены в файл: save_api_info_json.txt.')

    # Проводим фильтрацию списка по стране регистрации.
    country = input("Введите название страны для фильтрации по стране регистрации: ")
    country_filter = Aeroplane.search_plane_country_of_registration(get_aeroplanes_country_obj, country)
    print(country_filter)

    # Выводим Топ самолетов по высоте полета.
    top_n = int(input("Введите количество самолетов для вывода в топ N по высоте: "))
    altitude_sorted = Aeroplane.top_geo_altitude(country_filter, top_n)

    # Предлагаем ввести диапозон скорости для поиска, фильтрации и сортировки по заданным параметрам.
    speed_input = input("Введите минимальный и максимальный диапазон высот полета через запятую\n"
                         "(Пример: 50, 200): ").split(',')
    result = Aeroplane.speed_filter(altitude_sorted, speed_input)

    print('Ваш результат представлен в следующем списке:')
    for i in result:
        print(i)


if __name__ == "__main__":
    user_interaction()

# Canada
# 1600, 8000