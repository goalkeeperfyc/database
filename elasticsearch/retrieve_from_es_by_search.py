# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:03:53 2018

@author: fangyucheng
"""

from elasticsearch import Elasticsearch

hosts = '192.168.17.11'
port = 80
user_id = 'fangyucheng'
password = 'VK0FkWf1fV8f'
http_auth = (user_id, password)
es_connection = Elasticsearch(hosts=hosts, port=port, http_auth=http_auth)

search_body = {'query':
    {'bool':
        {'filter':
            [{'range': 
                {'timestamp':
                    {'lte': 1540260623915}}}]}}}

es_search = es_connection.search(index='ott_csm_behavior_match_cross_date', 
                                 body=search_body, size=200)

es_data_lst = es_search['hits']['hits']

source_lst = []

for line in es_data_lst:
    data_dic = line['_source']
    source_lst.append(data_dic)


#special task
for line in source_lst:
    detail_lst = line['detail']
    csm_mdu = detail_lst[0]['csm_mdu']
    for detail_dic in detail_lst:
        detail_dic.pop('csm_mdu')
    line['csm_mdu'] = csm_mdu