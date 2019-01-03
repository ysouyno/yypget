#!/usr/bin/env python3

from urllib import request
from ..utils import *

url_list = []

def get_txt(page, title):
    pass

def get_txt_wrapper(urls, title):
    urls = urls.replace('\\x22', '')
    assert urls

    urls = urls.replace('\\', '')
    assert urls

    urls = re.findall(r'pageLoadUrl:.*\w', urls)[0].split(',')
    print('urls: %s' % urls)
    print('urls length: %s' % len(urls))

    for url in urls:
        if 'json' in url:
            url_list.append(url.split(':', 1)[1].replace('}', '').strip(']'))

    print("url_list length: %s" % len(url_list))

    for page in url_list:
        get_txt(page, title)

def wenku_baidu_download(url, output_dir = '.'):
    resp = request.urlopen(url)
    assert resp, resp.getcode() == 200
    print('resp.getcode: %s' % resp.getcode())

    data = resp.read()
    assert data

    data = data.decode('gb2312')
    assert data

    doc_title = r1(r'\'title\'\:\s+\'(.+)\'', data)
    assert doc_title
    print('doc_title: %s' % doc_title)

    doc_id = r1(r'\'docId\'\:\s+\'(.+)\'', data)
    assert doc_id
    print('doc_id: %s' % doc_id)

    doc_type = r1(r'\'docType\'\:\s+\'(.+)\'', data)
    assert doc_type
    print('doc_type: %s' % doc_type)

    wkinfo_htmlurls = r1(r'WkInfo.htmlUrls\s+\=\s+\'(.+)\'\;', data)
    assert wkinfo_htmlurls
    # print(wkinfo_htmlurls)

    if doc_type == 'doc':
        get_txt_wrapper(wkinfo_htmlurls, doc_title)

download = wenku_baidu_download
