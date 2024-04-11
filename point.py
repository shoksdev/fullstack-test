import math


class Point:
    def __init__(self, x=0, y=0):
        """Инициализация переменных"""

        self.x = x
        self.y = y

    def get_coordinates(self):
        """Получение координат"""

        return self.x, self.y

    def set_coordinates(self, x, y):
        """Изменения координат"""

        self.x = x
        self.y = y

    def get_distance(self, other_point):
        """Получение расстояния между координатами"""

        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


point1, point2 = Point(1, 2), Point(4, 6)

print(f'Координаты первой точки: {point1.get_coordinates()}')
print(f'Координаты второй точки: {point2.get_coordinates()}')
print(f'Расстояние между первой и второй точкой: {point1.get_distance(point2)}')

point1.set_coordinates(3, 5)
print(f'Новые координаты первой точки: {point1.get_coordinates()}')
print(f'Расстояние между первой и второй точкой после изменения координат: {point1.get_distance(point2)}')
