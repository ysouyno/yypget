#!/usr/bin/env python3

import requests
import os
from bs4 import BeautifulSoup
from tqdm import tqdm
from ..utils import *

# test url:
# https://sv.baidu.com/videoui/page/videoland?pd=bjh&context={%22nid%22:%224949783038993399443%22,%22sourceFrom%22:%22bjh%22}&fr=bjhauthor&type=video

def baidu_download(url, output_dir = '.'):
    r = requests.get(url)
    assert r.status_code == 200

    soup = BeautifulSoup(r.text, features = 'html.parser')
    find_result = soup.find(id = 'main-player')
    assert find_result

    # download
    video_real_url = find_result.video.source.attrs['src']
    assert video_real_url

    video = requests.get(video_real_url, stream = True)
    assert video.status_code == 200

    video_file = soup.title.string
    assert video_file

    ext = get_url_file_ext(video_real_url)
    assert ext

    video_file = video_file + '.' + ext
    video_file = os.path.join(output_dir, video_file)

    t = tqdm(total = int(video.headers['Content-Length']), ascii = True)

    with open(video_file, 'wb') as file:
        for chunk in video.iter_content(chunk_size = 1024):
            if chunk:
                file.write(chunk)
                t.update(len(chunk))

    t.close()

    print('download \"%s\" success' % video_file)

download = baidu_download
