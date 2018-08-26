# -*- coding: utf-8 -*-

import requests

import data_api as dapi


def getGroupsUser(user_id):
    """Функция для получения групп пользователя.
        Принимается числовой ID пользователя.
        Возвращается список ID групп пользователя.
    """

    try:
        params = {'user_id': user_id, 'v': '5.73', 'access_token': dapi.token, 'count': 20}
        response = requests.get("https://api.vk.com/method/groups.get", params)

        return response.json()['response']['items']
    except:
        print("\n###\nОшибка получения групп пользователя!\n###\n")
        return 1


def getFriendsUser(user_id):
    """Функция для получения друзей пользователя.
        Принимается числовой ID.
        Возвращается список ID друзей.
    """

    try:
        params = {'user_id': user_id, 'v': '5.73', 'access_token': dapi.token}
        response = requests.get("https://api.vk.com/method/friends.get", params)

        return response.json()['response']['items']
    except:
        print("\n###\nОшибка при получении друзей пользователя\n###\n")
        return 1


def getPost(ids, mode='user'):
    """Функция для получения постов группы или пользователя в зависимости от режима (mode).
        Параметры:
            :ids: Список или одиночный ID пользователей или групп.;
            :mode: Режим 'group' или 'users'. По умолчанию 'user'.
    """

    if type(ids) != list:
        ids = [ids]
    
    for i in range(len(ids)):
        if not ids[i].isdigit():
            ids[i] = getId(ids[i], mode=mode)

    list_posts = []
    counter = 0
    count = 50
    while counter < len(ids):
        if mode == "group":
            #ids[counter] = -ids[counter]
            count = 100

        params = {'v': '5.73', "access_token": dapi.token,
                  'owner_id': ids[counter], 'count': count, "offset": 0}
        try:
            response = requests.get("https://api.vk.com/method/wall.get", params)
            if "error" in response.json():
                if response.json()["error"]["error_code"] == 6:
                    continue
                else:
                    counter += 1
                    continue
        except:
            print("Ошибка")
        else:
            list_posts.append(response.json()['response']['items'])
            counter += 1

    return list_posts[0]


def getId(ids, mode='user'):
    """Функция для получения цифрового ID пользователя или группы.
    Принимаемые параметры:
        :ids: короткое имя пользователя или группы
        :mode: для чего искать ID: пользователя или группы ('user', 'group').
        По умолчанию поиск осуществляется для 'user'.
    """

    if mode == 'user':
        params = {'v': '5.73', "access_token": dapi.token, 'user_ids': ids}
        response = requests.get("https://api.vk.com/method/users.get", params)

        return response.json()['response'][0]['id']
    elif mode == 'group':
        params = {'v': '5.80', "access_token": dapi.token, 'group_ids': ids}
        response = requests.get("https://api.vk.com/method/groups.getById", params)
        return '-' + str(response.json()['response'][0]['id'])


def getUserInfo(user_id, setfields: tuple=('city',)):
    """Функция для получения информации о пользователе.
    Принимаемые параметры:
        :user_id: индификатор пользователя (числовой или короткое имя);
        :fields: параметры, которые необходимо получить (Передвать кортеж!). По умолчанию только 'city'.
    Возвращает json-структуру со значениями переданных параметров.
    Пример:
        :запрос: getUserInfo('parametist', ('city', 'home_town'));
        :ответ: {'city': {'id': 147, 'title': 'Тюмень'}, 'home_town': 'Тюмень'}.
    """

    fields = ''.join([i+',' for i in setfields])[:-1]
    params = {'v': '5.73', "access_token": dapi.token, 'user_ids': user_id, 'fields': fields}
    response = requests.get("https://api.vk.com/method/users.get", params).json()['response'][0]
    response = {k: v for k, v in response.items() if k in setfields}

    return response


def getLikePost(ids, post_id):
    """Функция для получения лайков поста.
        Принимает:
            :ids: числовой ID группы или пользователя;
            :post_id: числовой ID поста.
        Возвращает список лайкнувших.
    """

    params = {'type': 'post', 'owner_id': ids, 'item_id': post_id,
              'filter': 'likes', 'friends_only': 0, 'extended': 1,
              'offset': 0, 'count': 200, 'skip_own': 0, 'v': '5.80', 'access_token': dapi.token}
    response = requests.get('https://api.vk.com/method/likes.getList', params).json()['response']

    return response
