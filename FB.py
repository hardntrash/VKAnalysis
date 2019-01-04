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
    return graph.get_object(obj_name, fields='id')