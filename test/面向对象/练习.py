"""
公路（Road):
    属性：公路名称，公路长度
车 （car):
    属性：车名，时速
    方法：1.求车名在那条公路上以多少时速行驶了都吃，
        get_time(self,road)
        2.初始化车属性信息__init__方法
        3、打印显示车属性信息
"""


class Road(object):
    def __init__(self, road_name, road_len):
        self.road_name = road_name
        self.road_len = road_len
        print(self.road_name, self.road_len)


class Car(object):
    def __init__(self, car_name, speed):
        self.car_name = car_name
        self.speed = speed
        # print(self.car_name, self.speed)

    def __str__(self):
        return "%s-%d" % (self.car_name, self.speed)

    def get_time(self):
        pass


r = Road("泰山路", "2000")  # r和road指向同一个地址空间
golf = Car("高尔夫", 50)
print(golf)
#Car.get_time(1000)

Road.road_len
Car.speed
