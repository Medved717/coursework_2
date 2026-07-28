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

    @staticmethod
    def get_plane(plane):
        return Aeroplane(country_of_registration=plane[2] if plane[2] else 'Неизвестно',
                         call_sign=plane[1] if plane[1] else 'Неизвестно',
                         velocity=plane[9] if plane[9] is not None else 0.0,
                         geo_altitude=plane[13]if plane[13] is not None else 0.0)


