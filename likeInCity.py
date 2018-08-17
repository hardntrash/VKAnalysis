# -*- coding: utf-8 -*-

from geocoder import google as coords

from VK import getLikePost
from VK import getUserInfo


def counterLike(ids, post_id):
    """Функция для нахождения количества лайкнувших из городов.
        Принимает:
            :ids: числовой ID группы или пользователя;
            :post_id: числовой ID поста.
        Возвращает список лайкнувших.
    """

    listId = [i['id'] for i in getLikePost(ids, post_id)['items']]
    
    cityes = {}

    for i in listId:
        city = getUserInfo(i)
        print('City', city)
        if city != {}:
            city = city['city']['title']
        else:
            continue
        if city not in cityes.keys():
            crds = coords(city).latlng
            print('Coords', crds)
            if crds == None:
                continue
            cityes.update({
                city : {
                    'like_count' : 1,
                    'latitude' : crds[0],
                    'longitude' : crds[1]
                }
            })
        else:
            cityes[city]['like_count'] += 1

    return cityes
