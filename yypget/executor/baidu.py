#!/usr/bin/env python3

from urllib import request
import os
import sys
from ..utils import *

# test url:
# https://sv.baidu.com/videoui/page/videoland?pd=bjh&context={%22nid%22:%224949783038993399443%22,%22sourceFrom%22:%22bjh%22}&fr=bjhauthor&type=video

def urlretrieve_callback(count, size, total):
    sys.stdout.write('\rcount: %s, size: %s, total: %s' % (count, size, total))
    sys.stdout.flush()

def baidu_download(url, output_dir = '.'):
    resp = request.urlopen(url)
    assert resp, resp.getcode() == 200

    data = resp.read()
    assert data

    data = data.decode('utf-8')

    title = r1(r'<title>(.*)</title>', data)
    assert title

    true_url = r1(r'video-src="(.*)"><video', data)
    assert true_url

    video = request.urlopen(true_url)
    assert video, video.getcode() == 200

    ext, size = get_url_file_ext_size(true_url)

    video_file = title + '.' + ext
    video_file = os.path.join(output_dir, video_file)

    request.urlretrieve(true_url, video_file, urlretrieve_callback)
    print('\ndownload success: %s' % video_file)

download = baidu_download
