# -*- coding: utf-8 -*-

from geocoder import yandex as coords

from VK import getLikePost
from VK import getUserInfo
from VK import getId


def counterLike(ids, post_id, mode='user'):
    """Функция для нахождения количества лайкнувших из городов.
        Принимает:
            :ids: числовой ID группы или пользователя;
            :post_id: числовой ID поста.
        Возвращает список лайкнувших.
    """  
    ids = str(ids)

    if not ids.isdigit():
        ids = getId(ids, mode=mode)

    listId = [i['id'] for i in getLikePost(ids, post_id)['items']]

    cityes = {}

    for i in listId:
        city = getUserInfo(i)
        if city != {}:
            city = city['city']['title']
        else:
            continue
        if city not in cityes.keys():
            crds = coords(city).latlng
            if crds == None:
                continue
            cityes.update({
                city: {
                    'like_count': 1,
                    'latitude': crds[0],
                    'longitude': crds[1]
                }
            })
        else:
            cityes[city]['like_count'] += 1

    return cityes
