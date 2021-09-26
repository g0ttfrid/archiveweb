# archiveweb
Fetch all the URLs that Google and Wayback Machine knows of the target except:
- for image, css and other static files
- urls with same path but parameter value difference


```

 █████╗ ██████╗  ██████╗██╗  ██╗██╗██╗   ██╗███████╗    ██╗    ██╗███████╗██████╗
██╔══██╗██╔══██╗██╔════╝██║  ██║██║██║   ██║██╔════╝    ██║    ██║██╔════╝██╔══██╗
███████║██████╔╝██║     ███████║██║██║   ██║█████╗      ██║ █╗ ██║█████╗  ██████╔╝
██╔══██║██╔══██╗██║     ██╔══██║██║╚██╗ ██╔╝██╔══╝      ██║███╗██║██╔══╝  ██╔══██╗
██║  ██║██║  ██║╚██████╗██║  ██║██║ ╚████╔╝ ███████╗    ╚███╔███╔╝███████╗██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝     ╚══╝╚══╝ ╚══════╝╚═════╝
                                                                            v1.1

usage: archiveweb.py [arg] target|url_list

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Insert domain or subdomain
  -f FILE, --file FILE  Insert domain or subdomain list
  -x ONLY_EXT, --only_ext ONLY_EXT
                        get result with specific extension
```

Usage:

```
▶ git clone https://github.com/g0ttfrid/archiveweb && cd archiveweb

▶ pip3 install -r requirements.txt

▶ python3 archiveweb.py -t example.com
```


### Inspired by

[dorks-eye](https://github.com/BullsEye0/dorks-eye)\
[waybackurls](https://github.com/tomnomnom/waybackurls)\
[uro](https://github.com/s0md3v/uro)
