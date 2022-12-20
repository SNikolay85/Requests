import requests
from time import *
import json

today = int(time())
two_days_ago = today - 86400
num_page = 1

def qu(num_page, count_quest=0, today=today, two_days_ago=two_days_ago):
    counter = 0
    url = f'https://api.stackexchange.com/2.3/questions?page={num_page}&pagesize=100&fromdate={two_days_ago}&todate={today}&order=desc&sort=creation&tagged=python&site=stackoverflow'
    response = requests.get(url)
    data = json.loads(response.text)
    for question in data['items']:
        counter += 1
        count_quest += 1
        print(f" Вопрос: {question['title']}")
        print(f" Теги: {question['tags']}")
        print(f" Дата создания: {ctime(question['creation_date'])}")
        print()
    if data['has_more'] == False:
        print('The end')
        print(f'Всего вопросов: {count_quest}')
    else:
        if counter == 100:
            num_page += 1
            count_quest += 100
            qu(num_page, count_quest)

qu(num_page)



