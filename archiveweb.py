#!/usr/bin/python3
import requests
import argparse
from urllib.parse import urlparse
from googlesearch import search
from tqdm import tqdm

exts = ('.css', '.png', '.pdf', '.jpg', '.jpeg', '.ico', '.bmp', '.svg', '.gif', '.woff', '.woff2', '.ttf')

def parse_args():
    parser = argparse.ArgumentParser(usage='archiveweb.py -t example.com -f output-example.txt')
    parser.add_argument('-t', '--target', type=str, required=True)
    parser.add_argument('-o', '--output_file', type=argparse.FileType('w', encoding='utf-8'), required=True)
    return parser.parse_args()

def dorks(target):
    print('[+] Google dorks')
    data = []
    try:
        for value in tqdm(search(f'site:{target}', start=0, stop=None, pause=2)):
            if not any(x in value.split('/')[-1] for x in exts):
                data.append(value)
    except Exception:
        if 'HTTP Error 429' in value:
            print('[!] HTTP Error 429: Too Many Requests')
            print('[!] try later...')
        else:
            print('[!] Error in google search')
    return sorted(set(data))

def wayback(target):
    print('\n[+] Wayback machine')
    data = []
    try:
        r = requests.get(f'http://web.archive.org/cdx/search/cdx?url={target}/*&output=json&collapse=urlkey')
        for value in tqdm(r.json()):
            if not any(x in value[2].split('/')[-1] for x in exts) and 'http' in value[2]:
                data.append(value[2])
    except Exception:
        print('[!] Error in wayback machine')
    return sorted(set(data))

def clear(list):
    print('\n[+] Clear list')
    data = []
    temp = []
    urls = sorted(set(list))
    for url in tqdm(urls):
        u = urlparse(url)
        if not u.query:
            data.append(url.rstrip())
        if u.query and '&' not in u.query:
            param = u.query.split('=')[0]
            x = f'{u.scheme}{u.netloc}{u.path}{param}'
            if x not in temp:
                temp.append(x)
                data.append(url.rstrip())
        if '&' in u.query:
            param = u.query.split('&')
            concat = ''
            for p in param:
                c = f'{p.split("=")[0]}'
                concat += c
            x = f'{u.scheme}{u.netloc}{u.path}{sorted(concat)}'
            if x not in temp:
                temp.append(x)
                data.append(url.rstrip())
    return data

def main():
    try:
        args = parse_args()
        data = clear([*dorks(args.target), *wayback(args.target)])
        output = args.output_file
        output.write('\n'.join(data))
    except KeyboardInterrupt:
        print('[!] Stopping')

if __name__ == '__main__':
    main()
