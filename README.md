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

usage: archiveweb.py -t example.com

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        insert domain/subdomain
  -f FILE, --file FILE  insert list w/ domains/subdomains
  -x EXT, --ext EXT     get result w/ specific extensions (-x asp,aspx)

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
