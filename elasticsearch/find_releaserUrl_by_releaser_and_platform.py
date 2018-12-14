# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:37:26 2018

@author: fangyucheng
"""


import elasticsearch
import elasticsearch.helpers
from crawler.crawler_sys.utils.trans_format import csv_to_lst_with_headline
from crawler.crawler_sys.utils.trans_format import lst_to_csv

hosts = '192.168.17.11'
port = 80
user_id = 'fangyucheng'
password = 'VK0FkWf1fV8f'
http_auth = (user_id, password)
lose_re_url = []
es = elasticsearch.Elasticsearch(hosts=hosts, port=port,
                                 http_auth=http_auth)

task_lst = csv_to_lst_with_headline('F:/add_target_releaser/Nov/zhangqiongzi_keycustom.csv')

for line in task_lst:
    releaser = line['releaser']
    platform = line['platform']
    search_body = {"query": {"bool": {"filter": [{"term": {"platform.keyword": platform}},
                                                 {"term": {"releaser.keyword": releaser}}]}}}

    es_search = es.search(body=search_body,
                          index='target_releasers',
                          doc_type='doc')
    hits = es_search['hits']['total']
    if hits != 0:
        releaserUrl = es_search['hits']['hits'][0]['_source']['releaserUrl']
        line['releaserUrl'] = releaserUrl

lst_to_csv(listname=task_lst,
           csvname='F:/add_target_releaser/Nov/zhangqiongzi_kc2.csv')