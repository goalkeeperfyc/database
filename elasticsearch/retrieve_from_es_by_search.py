# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:03:53 2018

@author: fangyucheng
"""

from elasticsearch import Elasticsearch
from crawler.crawler_sys.utils import trans_format

hosts = '192.168.17.11'
port = 80
user_id = 'fangyucheng'
password = 'VK0FkWf1fV8f'
http_auth = (user_id, password)
es_connection = Elasticsearch(hosts=hosts, port=port, http_auth=http_auth)

search_body = {"query": {"bool":{"filter":[{"term":{"platform.keyword":"haokan"}},{"term":{"frequency":9}}]}}}

es_search = es_connection.search(index='target_releasers', doc_type='doc',
                                 body=search_body, size=200)

es_data_lst = es_search['hits']['hits']

source_lst = []

for line in es_data_lst:
    data_dic = line['_source']
    source_lst.append(data_dic)

trans_format.lst_to_csv(listname=source_lst, csvname='haokan_high_fre_releasers.csv')