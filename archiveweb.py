#!/usr/bin/python3
import argparse
import requests
from googlesearch import search

exts = ('.css', '.png', '.pdf', '.jpg', '.jpeg', '.ico', '.bmp', '.svg', '.gif', '.woff', '.woff2', '.ttf')

def parse_args():
    parser = argparse.ArgumentParser(usage='archiveweb.py -t xxx.example.com')
    parser.add_argument('-t', '--target', type=str, required=True)
    return parser.parse_args()

def dorks(target):
    data = []
    for r in search(f"site:{target}", start=0, stop=None, pause=2):
        if any(x in r.split('/')[-1] for x in exts) == False:
            data.append(r)
    data = sorted(set(data))
    return data

def wayback(target):
    data = []
    r = requests.get(f"http://web.archive.org/cdx/search/cdx?url={target}/*&output=json&collapse=urlkey")
    for (key,value) in enumerate(r.json()):
        if any(x in value[2].split('/')[-1] for x in exts) == False:
            data.append(value[2])
    data = sorted(set(data))
    return data

def main():
    args = parse_args()
    data = dorks(args.target) + wayback(args.target)
    data = sorted(set(data))
    for d in data:
        if 'http' in d: print(d) 
            
main()