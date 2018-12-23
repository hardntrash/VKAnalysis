# -*- coding: utf-8 -*-

import facebook as FB
import data_api as dapi

graph = FB.GraphAPI(access_token=dapi.fb.page_token)

def getFeed(group_id):
    feed = graph.get_object(group_id+'/feed')

    try:
        return feed['data']
    except:
        return []



def getId(obj_name):
    """Функция для получения цифрового ID пользователя или группы.
    Принимаемые параметры:
        :ids: короткое имя пользователя или группы
        :mode: для чего искать ID: пользователя или группы ('user', 'group').
        По умолчанию поиск осуществляется для 'user'.
    """

    return graph.get_object(obj_name, fields='id')


#ids = getId('Word Rate')
#print(ids)
