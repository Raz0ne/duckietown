import cv2


class TrafficSign:
    def __init__(self, name: str, img, influence: bool = False, desc: str = None):
        self.name = name
        self.desc = desc
        self.img = img
        self.influence = influence

    def show(self, window):
        pass


Stop = TrafficSign(name='Стоп',
                   desc='Запрещается движение без остановки перед стоп-линией. '
                        'Водитель должен уступить дорогу транспортным средствам, движущимся по пересекаемой дороге.',
                   influence=True,
                   img=cv2.imread('images/traffic_signs/stop.png'))

Yield = TrafficSign(name='Уступите дорогу',
                    desc='Водитель должен уступить дорогу транспортным средствам, движущимся по пересекаемой дороге',
                    influence=True,
                    img=cv2.imread('images/traffic_signs/yield.png'))

NoRightTurn = TrafficSign(name='Поворот направо запрещён',
                          influence=True,
                          img=cv2.imread('images/traffic_signs/no_right_turn.png'))

NoLeftTurn = TrafficSign(name='Поворот налево запрещён',
                         influence=True,
                         img=cv2.imread('images/traffic_signs/no_left_turn.png'))

DoNotEnter = TrafficSign(name='Въезд запрещён',
                         desc='Запрещается въезд всех транспортных средств в данном направлении.',
                         influence=True,
                         img=cv2.imread('images/traffic_signs/do_not_enter.png'))

OneWayRight = TrafficSign(name='Выезд на дорогу с односторонним движением направо',
                          desc='Знак информирует о выезде на дорогу с односторонним движением направо и запрещает вам '
                               'поворачивать навстречу одностороннему движению.',
                          influence=True,
                          img=cv2.imread('images/traffic_signs/one_way_right.png'))

OneWayLeft = TrafficSign(name='Выезд на дорогу с односторонним движением налево',
                         desc='Знак информирует о выезде на дорогу с односторонним движением налево и запрещает вам '
                              'поворачивать навстречу одностороннему движению.',
                         influence=True,
                         img=cv2.imread('images/traffic_signs/one_way_left.png'))

FourWay_Intersect = TrafficSign(name='Перекрёсток с возможным движением налево, прямо и направо',
                                desc='Знак предупреждает о приближении перекрёстка.',
                                img=cv2.imread('images/traffic_signs/4_way_intersect.png'))

RightT_Intersect = TrafficSign(name='Перекрёсток с возможным движением прямо и направо',
                               desc='Знак предупреждает о приближении перекрёстка.',
                               img=cv2.imread('images/traffic_signs/right_T_intersect.png'))

LeftT_Intersect = TrafficSign(name='Перекрёсток с возможным движением налево и прямо',
                              desc='Знак предупреждает о приближении перекрёстка.',
                              img=cv2.imread('images/traffic_signs/left_T_intersect.png'))

T_Intersect = TrafficSign(name='Перекрёсток с возможным движением налево и направо',
                          desc='Знак предупреждает о приближении перекрёстка.',
                          img=cv2.imread('images/traffic_signs/T_intersect.png'))

Pedestrian = TrafficSign(name='Пешеходный переход',
                         desc='Водителю ТС следует сбросить скорость. Знак информирует о нахождении пешеходного '
                              'перехода на данном участке дороги.',
                         img=cv2.imread('images/traffic_signs/pedestrian.png'))

T_LightAhead = TrafficSign(name='Светофорное регулирование',
                           desc='Перекресток, пешеходный переход или участок дороги, движение на котором регулируется '
                                'светофором.',
                           img=cv2.imread('images/traffic_signs/T_light_ahead.png'))

DuckCrossing = TrafficSign(name='Утячий переход',
                           desc='Водителю ТС следует сбросить скорость. Знак информирует о том, что дорогу на данном '
                                'участке могут переходить утки.',
                           img=cv2.imread('images/traffic_signs/duck_crossing.png'))

Parking = TrafficSign(name='Парковка',
                      img=cv2.imread('images/traffic_signs/parking.png'))
