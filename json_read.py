# _*_ coding: utf-8 _*_
import json
import sys
sys.setdefaultencoding('utf-8')

with open('books.json', 'r') as f:
    json_dict = json.loads(f.read(), "utf-8")
#book = 'book1の情報：{}'.format(json_dict['本1'.encode('UTF-8')])
print('book1の情報：{}'.format(json_dict['book1']['title']))
#print(json_dict['book1']['title'])
print('book3のページ数:{}'.format(json_dict['book3']['page']))
