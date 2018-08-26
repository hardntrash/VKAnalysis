# -*- coding: utf-8 -*-

# Этот файл с примером использования некоторых функций.
# 
# Функция 'counterLike' считывает количество лайков под постом,
# собирает города лакнувших и составляет статистику лайков по городам,
# прикрепляя к этим городам их долготу и широту.
# Принимаемые параметры:
#   :ids: ID пользователя или группы;
#   :post_id: ID самой записи(поста);
#   :mode: 'user' или 'group' в зависимости, что нужно. По умолчанию 'user'.
# Данная функция возвращает словарь в виде:
# {
#   'city_1' : {
#        'like_count': number,
#        'latitude': 'value',
#        'longitude': 'value'
#   },
#   'city_2' : {
#        'like_count': number,
#        'latitude': 'value',
#        'longitude': 'value'
#   }
# }
# 
# Функция 'getPost' получает список постов группы или пользователя.
# Принимает:
#   :ids: пользователя или группы;
#   :mode: 'user' или 'group' в зависимости, что нужно. По умолчанию 'user'.
# 
# Возвращает список словарей с различными данными данными. 
# 
# Функция geiId возврашает цифровой ID пользователя или группы.
# Принимает:
#   :ids: краткое имя;
#   :mode: 'user' или 'group' в зависимости, что нужно. По умолчанию 'user'.
# 

from likeInCity import counterLike
from VK import getId
from VK import getPost

#   Посик инфоомации последнего поста (number_post)
#   Заполни данные:
number_post = 1   # Не больше 49 для 'user' и не больше 99 для 'group'
ids = 'myironcomp'
mode = 'group'

post_id = getPost(ids, mode=mode)[number_post]['id']

print(counterLike(ids, post_id, mode=mode))