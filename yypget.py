import sys, getopt
import re
import argparse
from yypget import *

def r1(pattern, text):
    m = re.search(pattern, text)
    if m:
        return m.group(1)

def download_wrapper(url, output_dir = '.'):
    host = r1(r'https?://([^/]+)/', url)
    assert(host)
    print('host: %s' % host)

    if host.endswith('.com.cn'):
        host = host[:-3]
        print('host: %s' % host)

    domain = r1(r'(\.[^.]+\.[^.]+)$', host)
    assert(domain)
    print('domain: %s' % domain)

    site = r1(r'([^.]+)', domain)
    assert(site)
    print('site: %s' % site)

    supported_sites = {
        'baidu': baidu,
    }

    if site in supported_sites:
        m = supported_sites[site]
    else:
        raise NotImplementedError(site)

    m.download(url, output_dir = output_dir)

def main(download):
    parser = argparse.ArgumentParser()
    parser.add_argument('url', metavar = 'URL')
    parser.add_argument('-o', '--output-dir', help = 'set output directory')

    url = ''
    output_dir = '.'

    args = parser.parse_args()
    if args.url:
        url = args.url
        print('url: %s' % url)

    if args.output_dir:
        output_dir = args.output_dir
        print('output_dir: %s' % output_dir)

    download(url, output_dir)

if __name__ == '__main__':
    main(download_wrapper)
