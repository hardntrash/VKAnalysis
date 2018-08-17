# -*- coding: utf-8 -*-

import requests
import data_api as dapi

def getGroupsUser(user_id):
    try:
        params = {'user_id' : user_id, 'v' : '5.73', 'access_token' : dapi.token, 'count': 20}
        response = requests.get("https://api.vk.com/method/groups.get", params)
        return response.json()['response']['items']
    except:
        print("\n###\nОшибка получения групп пользователя!\n###\n")
        return 1

def getFriendsUser(user_id):
    try:
        params = {'user_id' : user_id, 'v' : '5.73', 'access_token' : dapi.token}
        response = requests.get("https://api.vk.com/method/friends.get", params)
        return response.json()['response']['items']
    except:
        print("\n###\nОшибка при получении друзей пользователя\n###\n")
        return 1

def getPost(ids, mode):
    list_posts = []
    counter = 0
    count = 50
    while counter < len(ids):
        if mode == "groups":
            ids[counter] = -ids[counter]
            count = 100

        params = {'v' : '5.73', "access_token" : dapi.token, 'owner_id' : ids[counter], 'count' : count, "offset" : 0}
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
    return list_posts

def getUserId(user_id):
    params = {'v' : '5.73', "access_token" : dapi.token, 'user_ids' : user_id}
    response = requests.get("https://api.vk.com/method/users.get", params)
    return response.json()["response"][0]['id']

def getUserInfo(user_id, setfields:tuple=('city',)):
    """Функция для получения информации о аользователе.
    Принимаемые параметры:
        :user_id: индификатор пользователя (числовой или короткое имя);
        :fields: параметры, которые необходимо получить (Передвать кортеж!). По умолчанию только 'city'.
    Возвращает json-структуру со значениями переданных параметров.
    Пример:
        :запрос: getUserInfo('parametist', ('city', 'home_town'));
        :ответ: {'city': {'id': 147, 'title': 'Тюмень'}, 'home_town': 'Тюмень'}.
        """
    fields = ''.join([i+',' for i in setfields])[:-1]
    params = {'v' : '5.73', "access_token" : dapi.token, 'user_ids' : user_id, 'fields' : fields}
    response = requests.get("https://api.vk.com/method/users.get", params).json()['response'][0]
    response = {k : v for k, v in response.items() if k in setfields}
    return response