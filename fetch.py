#!/usr/bin/env python3
import requests
import re
from urllib.parse import unquote
import base64

def decode_email(email_str):
    # 方法来自 https://zhuanlan.zhihu.com/p/36912486
    email_list = re.findall(r'.{2}',email_str)
    key = email_list[0]
    ll = []

    for e in email_list[1:]:
        # 对十六进制进行异或运算
        r = hex(int(key,16) ^ int(e,16))
        ll.append(r)

    # 拼接运算后的字符串
    a = ''.join(ll)
    # URL解码字符串
    email = unquote(a.replace('0x','%'))
    return email


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}

res = requests.get("https://vpnbay.com/free-ss-vmess-trojan-nodes.html",headers=headers)

merge = []

for url, _ in re.findall(r"((vmess|ss|trojan|ssr)://.*?)<br />",res.text):
    if "email-protection" in url:
        host = decode_email(re.search(r'data-cfemail="(.*?)"',url).group(1))
        merge.append(re.sub("<a.*?>.*?</a>",host,url))
    else:
        merge.append(url)

txt = ''

for url in set(merge):
    txt = txt + url + '\n'

with open("list_raw.txt",'w') as f:
    f.write(txt)

with open("list.txt",'w') as f:
    b64txt = base64.b64encode(txt.encode())
    f.write(str(b64txt,'utf-8'))
