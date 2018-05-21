import requests
from bs4 import BeautifulSoup

#url = "https://python123.io/ws/demo.html"
url = "https://sh.lianjia.com/ershoufang/rs"
#url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
kv={'rs':'曲阳'}
try:
    r = requests.get(url,params=kv)
#    r.text
    demo=r.text
#    r.raise_for_status()
#    r.encoding = r.apparent_encoding
#    print(demo)
    soup = BeautifulSoup(demo, 'html.parser')
    tag=soup.span.parent.name
    print(tag)
    #print(soup.prettify())
except:
    print("爬取失败")