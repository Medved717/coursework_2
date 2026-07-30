import requests
from src.api_service import APIAdapter
from src.plane_service import Aeroplane
from src.work_files import EditingFiles

data = [Aeroplane("Canada", "JZA427", 123.74, 2263.14),
        Aeroplane("Canada", "ET835", 99.82, 2049.78),
        Aeroplane("Canada", "WJA77", 220.47, 11475.72),
        Aeroplane("Canada", "WJA611", 171.32, 9525),
        Aeroplane("Canada", "CFMYW", 69.86, 3093.72),
        Aeroplane("Canada", "ROU1757", 228.92, 8526.78),
        Aeroplane("France", "ROU2440", 213.29, 7741.92),
        Aeroplane("Canada", "PRO4805", 65.12, 167.64),
        Aeroplane("Canada", "CFTOQ", 113.95, 3718.56),
        Aeroplane("Russia", "", 69.55, 1539.24),
        Aeroplane("Canada", "ACA408", 0, 0.0),
        Aeroplane("Canada", "WJA102", 142.02, 3002.28),
        Aeroplane("Canada", "ACA845", 228.89, 12283.44),
        Aeroplane("Canada", "MBK860", 105.52, 6896.1),
        Aeroplane("Canada", "JZA7985", 135.67, 1729.74),
        Aeroplane("Spain", "CGVFD", 56.59, 2438.4),
        Aeroplane("Canada", "CFUOW", 87.36, 1562.1),
        Aeroplane("Canada", "CGBRX", 94.03, 3124.2),
        Aeroplane("Canada", "TSC293", 219.07, 10774.68),
        Aeroplane("Canada", "SYB021", 278.17, 14196.06),
        Aeroplane("Canada", "TSC603", 181.81, 4274.82),
        Aeroplane("Canada", "CGOFP", 78.69, 868.68),
        Aeroplane("Canada", "ROU1997", 168.91, 3429),
        Aeroplane("Canada", "ACA851", 260.84, 11704.32),
        Aeroplane("Canada", "ROU1901", 228.53, 9982.2),
        Aeroplane("Canada", "SUT1212", 134.8, 6675.12)]

def present_country(data):
    """Получаем список самолетов и выводим только
    список доступных стран по регистрации самолетов."""

    if not data:
        print('Список стран пуст ввиду отсутствия самолетов по введенным критериям.')
        return None
    else:
        list_country = []

        for plane in data:
            if plane.country_of_registration not in list_country:
                list_country.append(plane.country_of_registration)
        return list_country


a = present_country(data)
for i in a:
    print(i)