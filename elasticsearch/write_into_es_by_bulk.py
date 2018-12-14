# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:02:49 2018

@author: fangyucheng
"""

import json
from elasticsearch import Elasticsearch


hosts = '192.168.17.11'
port = 80
user_id = 'fangyucheng'
password = 'VK0FkWf1fV8f'
http_auth = (user_id, password)
lose_re_url = []
es = Elasticsearch(hosts=hosts, port=port, http_auth=http_auth)

bulk_all_body = ''

#input_lst = meta.dic_file_to_lst('D:/CCR/added_target_releaser/hubei/crawler_腾讯视频_on_2018-08-13_json')

for releaser_dict in result_list:
    releaser = releaser_dict['releaser']
    platform = releaser_dict['platform']
    _id = platform + '_' + releaser
    bulk_head = '{"index": {"_id":"%s"}}' % _id
    data_str = json.dumps(releaser_dict, ensure_ascii=False)
    bulk_one_body = bulk_head+'\n'+data_str+'\n'
    bulk_all_body += bulk_one_body
    es.bulk(index='target_releasers', doc_type='doc',
            body=bulk_all_body)
    bulk_all_body = ''
    print('write %s into es' % releaser)
#