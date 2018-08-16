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

def getUserInfo():
    pass