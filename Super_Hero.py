import requests
import json

heroes = {}
def get_hero(self):
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    data = json.loads(response.text)
    for hero in data:
        if hero['name'] == self:
            heroes[self] = hero["powerstats"]["intelligence"]

get_hero('Hulk')
get_hero('Captain America')
get_hero('Thanos')

max_intelligence = dict(sorted(heroes.items(), key=lambda item: item[1]))
print(f'Самый умный супергерой: {list(max_intelligence.keys())[2]}')
