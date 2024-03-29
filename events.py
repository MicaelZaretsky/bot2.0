import datetime

event1 = {'name': "Тестовый первый запуск. Прошел ЧАС! ",
          'date': datetime.datetime.now()+ datetime.timedelta(seconds=15),
          'respawn': datetime.timedelta(minutes=30)}
event1_2 = {'name': "Торговщик сапфирами I(rpg, x: 65,z:580 y:47) Обновится через 1 минуту! ",
            'date': datetime.datetime(year=2024, month=3, day=18, hour=23, minute=45, second=10),
            'respawn': datetime.timedelta(hours=8)}
event2 = {'name': "Торговщик сапфирами I(Болото печали, x:685, z: 245, y:55) Обновился! ",
          'date': datetime.datetime(year=2024, month=3, day=9, hour=1, minute=18, second=50),
          'respawn': datetime.timedelta(hours=8)}
event2_2 = {'name': "Торговщик сапфирами I(Болото печали, x:685, z: 245, y:55) Обновится через 1 минуту! ",
            'date': datetime.datetime(year=2024, month=3, day=19, hour=3, minute=17, second=50),
            'respawn': datetime.timedelta(hours=8)}
event3 = {'name': "Торговщик сапфирами II(Болото печали, x:685, z: 245, y:55) Обновился! ",
          'date': datetime.datetime(year=2024, month=3, day=8, hour=3, minute=18, second=30),
          'respawn': datetime.timedelta(hours=8)}
event3_2 = {'name': "Торговщик сапфирами II(Болото печали, x:685, z: 245, y:55) Обновится через 1 минуту! ",
            'date': datetime.datetime(year=2024, month=3, day=8, hour=3, minute=17, second=30),
            'respawn': datetime.timedelta(hours=8)}

event4 = {'name': "Торговщик сапфирами II(Красногорье, x:173, z: -47, y:59) Обновился! ",
          'date': datetime.datetime(year=2024, month=3, day=8, hour=3, minute=18, second=15),
          'respawn': datetime.timedelta(hours=8)}
event4_2 = {'name': "Торговщик сапфирами II(Красногорье, x:173, z: -47, y:59) Обновится через 1 минуту! ",
            'date': datetime.datetime(year=2024, month=3, day=8, hour=3, minute=17, second=15),
            'respawn': datetime.timedelta(hours=8)}
event5 = {'name': "Торговщик сапфирами I(Красногорье, x:173, z: -47, y:59) Обновился! ",
          'date': datetime.datetime(year=2024, month=3, day=8, hour=3, minute=18, second=12),
          'respawn': datetime.timedelta(hours=8)}
event5_2 = {'name': "Торговщик сапфирами I(Красногорье, x:173, z: -47, y:59) Обновится через 1 минуту! ",
            'date': datetime.datetime(year=2024, month=3, day=8, hour=3, minute=17, second=12),
            'respawn': datetime.timedelta(hours=8)}


events = []

events.append(event1)
events.append(event1_2)
events.append(event2)
events.append(event2_2)
events.append(event3)
events.append(event3_2)
events.append(event4)
events.append(event4_2)
events.append(event5)
events.append(event5_2)
