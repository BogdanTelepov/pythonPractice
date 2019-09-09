import requests
import io
import json

token = '52ce71095c0cda6eff9145c5550feb10cb5f722436c5632fe5f6210bb5957225959e8ba175ea2eb0a2aa4'
count = 2476
offset = 1000


def download(url):
    r = requests.get(url, stream=True)
    filename = url.split('/')[-1]

    with open(filename, 'bw') as file:
        for chunk in r.iter_content(4096):
            file.write(chunk)


def write_json(data):
    with open('response_2.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_largest(size_dict):
    weight = {'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 'm': 10, 'x': 20, 'y': 30, 'z': 40, 'w': 50}
    size_dict['type'] = weight[size_dict['type']]
    return size_dict['type']


def main():
    # photos = json.load(open('response_2.json'))['response']['items']

    # for photo in photos:
    # sizes = photo['sizes']

    # max_size_url = max(sizes, key=get_largest)['src']
    # download(max_size_url)

    r = requests.get('https://api.vk.com/method/photos.get',
                     params={'owner_id': '284902877',
                             'v': '5.52',
                             'access_token': token,
                             'album_id': 'saved', 'photo_sizes': True, 'count': count, 'offset': offset})
    write_json(r.json())


# id = 284902877
# https://api.vk.com/method/users.get?user_id=210700286&v=5.52
# https://oauth.vk.com/authorize?client_id=7109735&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos&response_type=token&v=5.52

if __name__ == '__main__':
    main()
