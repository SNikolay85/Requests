import requests

class YaUploader:
    host = 'https://cloud-api.yandex.net'

    def __init__(self, token: str):
        self.token = token

    def upload(self, path):
        file_name = 'Hello.txt'
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': path, 'overwrite': True}
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', headers=headers, params=params)
        requests.put(response.json().get('href'), data=open(file_name, 'rb'), headers=headers)
        if response.ok:
            print("Success")

if __name__ == '__main__':

    path_to_file = 'Hello.txt'
    token = 'here will be token'
    uploader = YaUploader(token)
    uploader.upload(path_to_file)




