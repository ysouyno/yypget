#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

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
    print("real url: %s" % video_real_url)

    video_title = soup.title.string
    assert(video_title)
    print('title: %s' % video_title)

    video = requests.get(video_real_url, stream = True)
    with open(video_title + '.mp4', 'wb') as mp4:
        for chunk in video.iter_content(chunk_size = 1024 * 1024):
            if chunk:
                mp4.write(chunk)

    print('download done')

download = baidu_download
