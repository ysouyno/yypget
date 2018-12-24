import re
import requests

def r1(pattern, text):
    m = re.search(pattern, text)
    if m:
        return m.group(1)

def get_url_file_ext(url):
    resp = requests.get(url)
    assert resp.status_code == 200

    type = resp.headers['Content-Type']
    type_dict = {
        'video/3gpp': '3gp',
        'video/f4v': 'flv',
        'video/mp4': 'mp4',
        'video/webm': 'webm',
        'video/x-flv': 'flv'
    }

    assert type in type_dict, type

    return type_dict[type]
