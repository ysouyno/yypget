import sys, getopt
from yypget import *

def download_wrapper(url, output_dir = '.'):
    supported_sites = {
        'baidu': baidu,
    }

    m = supported_sites['baidu']
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
