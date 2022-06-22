#!/usr/bin/python3
import argparse
from requests import get
from urllib.parse import urlparse
from googlesearch import search
from tqdm import tqdm

ver = "1.1"

def parse_args():
    parser = argparse.ArgumentParser(usage='archiveweb.py -t example.com')
    parser.add_argument('-t', '--target', type=str, help='insert domain/subdomain')
    parser.add_argument('-f', '--file', type=open, help='insert list w/ domains/subdomains')
    parser.add_argument('-x', '--ext', type=str, help='get result w/ specific extensions (-x asp,aspx)')
    return parser.parse_args()

def dorks(target):
    print(f'\n\n[+] Target: {target.rstrip()}')
    print('+ Google dorks')
    data = set()

    try:
        for value in tqdm(search(f'site:{target}', start=0, stop=None, pause=3.0)):
            data.add(value)
    
    except Exception:
        print('[!] Error in google search')
    
    return data

def wayback(target):
    print('\n+ Wayback machine')
    data = set()
    
    try:
        r = get(f'http://web.archive.org/cdx/search/cdx?url={target}/*&output=json&collapse=urlkey')
        for value in tqdm(r.json()):
            data.add(value[2])
    
    except Exception:
        print('[!] Error in wayback machine')
    
    return data

def only_ext(list, ext):
    data = set()
    
    for url in list:
        if any(f'.{x}' in url.split('/')[-1] for x in ext):
            data.add(url.rstrip())
    
    if not data:
        print(f'[!] {ext} not found')
    
    return data

def remove_ext(list):
    data = set()
    ext = ('.css', '.png', '.pdf', '.jpg', '.jpeg', '.ico', '.bmp', '.svg', '.gif', '.woff', '.woff2', '.ttf', '.eot', '.otf')
    
    for url in list:
        u = urlparse(url)
        if not any(x in u.path.split('/')[-1] for x in ext) and 'http' in url:
            data.add(url.rstrip())
    
    return data

def clear(list):
    print('\n+ Organizing list')
    
    data = set()
    temp = set()
    
    urls = sorted(set(list))
    
    for url in tqdm(urls):
        u = urlparse(url)

        if not u.query:
            data.add(url.rstrip())
        
        if u.query and '&' not in u.query:
            param = u.query.split('=')[0]
            x = f'{u.scheme}{u.netloc}{u.path}{param}'
            if x not in temp:
                temp.add(x)
                data.add(url.rstrip())
        
        if '&' in u.query:
            param = u.query.split('&')
            concat = ''
            for p in param:
                c = f'{p.split("=")[0]}'
                concat += c
            x = f'{u.scheme}{u.netloc}{u.path}{sorted(concat)}'
            if x not in temp:
                temp.add(x)
                data.add(url.rstrip())
    
    return sorted(data)

def logger(target, list):
    with open(f'{target}.txt', 'w', encoding='utf-8') as f:
        for line in list:
            f.write(f'{line}\n')

if __name__ == '__main__':
    try:
        args = parse_args()

        if args.target:
            if args.ext:
                data = clear([*dorks(args.target), *wayback(args.target)])
                data = only_ext(data, args.ext.split(','))
                logger(args.target, data)
            else:
                data = clear(remove_ext([*dorks(args.target), *wayback(args.target)]))
                logger(args.target, data)
        
        elif args.file:
            for target in args.file:
                if args.ext:
                    data = clear([*dorks(target.rstrip()), *wayback(target.rstrip())])
                    data = only_ext(data, args.ext.split(','))
                    logger(target.rstrip(), data)
                else:
                    data = clear(remove_ext([*dorks(target.rstrip()), *wayback(target.rstrip())]))
                    logger(target.rstrip(), data)

        else:
            print('[!] No arguments')
            print('[!] Try archiveweb.py -h')
    
    except KeyboardInterrupt:
        print('\n\n[!] Stopping')
