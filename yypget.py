import sys, getopt
import re
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
    help = 'Usage: python3 yypget.py [URL]'

    short_opts = 'h'

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts)
    except getopt.GetoptError as err:
        print(err)
        print(help)
        sys.exit()

    for op, value in opts:
        if op == '-h':
            print(help)
            sys.exit()

    for url in args:
        print('input url: %s' % url)
        download(url)

if __name__ == '__main__':
    main(download_wrapper)
