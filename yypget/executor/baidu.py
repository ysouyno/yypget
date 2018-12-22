#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# test url:
# https://sv.baidu.com/videoui/page/videoland?pd=bjh&context={%22nid%22:%224949783038993399443%22,%22sourceFrom%22:%22bjh%22}&fr=bjhauthor&type=video

def baidu_download(url, output_dir = '.'):
    r = requests.get(url)
    assert(r.status_code == 200)

    soup = BeautifulSoup(r.text, features = 'html.parser')
    find_result = soup.find(id = 'main-player')
    assert(find_result)

    # download video
    video_real_url = find_result.video.source.attrs['src']
    assert(video_real_url)
    print('real url: %s' % video_real_url)

    video_title = soup.title.string
    assert(video_title)

    video_file = os.path.join(output_dir, video_title)

    video = requests.get(video_real_url, stream = True)
    assert(video.status_code == 200)

    t = tqdm(total = int(video.headers['Content-Length']))

    with open(video_file + '.mp4', 'wb') as mp4:
        for chunk in video.iter_content(chunk_size = 1024):
            if chunk:
                mp4.write(chunk)
                t.update(len(chunk))

    t.close()

    print('download \"%s.mp4\" success' % video_title)

download = baidu_download
