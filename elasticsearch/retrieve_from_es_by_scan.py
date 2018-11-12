#!usr/bin/python

"""
Created on Mon Oct 29 09:03:15 2018

@author: fangyucheng
"""

import elasticsearch
import elasticsearch.helpers
from crawler.crawler_sys.utils import trans_format

result_lst = []

hosts = '192.168.17.11'
port = 80
user_id = 'fangyucheng'
password = 'VK0FkWf1fV8f'
http_auth = (user_id, password)
es_connection = elasticsearch.Elasticsearch(hosts=hosts, port=port, http_auth=http_auth)


search_body = {
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "platform.keyword": "腾讯视频"
          }
        },
        {
          "term": {
            "data_provider.keyword": "CCR"
          }
        },
        {
          "range": {
            "duration": {
              "lt": 600
            }
          }
        }
      ]
    }
  }
}
es_scan = elasticsearch.helpers.scan(es_connection, query=search_body, 
                                     index='short-video-weekly', doc_type='daily-url-2018_w44_s1')


for line in es_scan:
    data_dic = line['_source']
    result_lst.append(data_dic)
    print("be patient the length of result_lst is %s" % len(result_lst))

trans_format.lst_to_csv(listname=result_lst,
                        csvname='F:/week44.csv')


