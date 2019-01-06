#!/usr/bin/env python3

from urllib import request
import json
import os
import sys
import math
from ..utils import *

# test url:
# https://tv.sohu.com/v/cGwvOTM1ODU4Mi85MDQxMjI4OS5zaHRtbA==.html

def urlretrieve_callback(count, size, total):
    sys.stdout.write('\rDownloading: [%d/%d]' % (count, math.ceil(total / size)))
    sys.stdout.flush()

def tv_sohu_download(url, output_dir = '.'):
    resp = request.urlopen(url)
    assert resp, resp.getcode() == 200

    data = resp.read()
    assert data

    data = data.decode('GBK')
    assert data
    # print(data)

    vid = r1(r',vid:\s+\'(.+)\'', data)
    assert vid
    # print(vid)

    """
    title = r1(r',title:\s+\'(.+)\'', data)
    assert title
    print(title)
    """

    query_info_url = 'https://my.tv.sohu.com/play/videonew.do?vid='
    query_info_url += vid
    # print(query_info_url)

    info_resp = request.urlopen(query_info_url)
    assert info_resp, info_resp.getcode() == 200

    info_data = info_resp.read().decode('GBK')
    assert info_data
    # print(info_data)

    info_json = json.loads(info_data)
    assert info_json
    # print(info_json)

    title = info_json['data']['tvName']
    print(title)

    num = info_json['data']['num']
    # print(num)

    if num == 1:
        total_bytes = info_json['data']['totalBytes']
        # print(total_bytes)

        video_file = title + '.mp4'
        output_dir = os.path.realpath(output_dir)
        video_file = os.path.join(output_dir, video_file)

        su = info_json['data']['su'][0]
        assert su
        # print(su)

        true_url_url = 'https://data.vod.itc.cn/ip?new='
        true_url_url += su
        print(true_url_url)

        true_url_resp = request.urlopen(true_url_url)
        assert true_url_resp, true_url_resp.getcode() == 200

        true_url_data = true_url_resp.read().decode('utf-8')
        assert true_url_data
        # print(true_url_data)

        true_url_json = json.loads(true_url_data)
        assert true_url_json
        # print(true_url_json)

        true_url = true_url_json['servers'][0]['url']
        assert true_url
        # print(true_url)

        request.urlretrieve(true_url, video_file, urlretrieve_callback)
        print('\nDownload OK: \"%s\"' % video_file)
    else:
        pass

download = tv_sohu_download
