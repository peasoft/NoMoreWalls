#!/usr/bin/env python3
import requests
import re
from urllib.parse import unquote
import base64
import traceback

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
merge = []

# ========== 抓取 vpnbay.com 的节点 ==========
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

try:
    res = requests.get("https://vpnbay.com/free-ss-vmess-trojan-nodes.html",headers=headers)
    for url, _ in re.findall(r"((vmess|ss|trojan|ssr)://.*?)<br />",res.text):
        if "email-protection" in url:
            host = decode_email(re.search(r'data-cfemail="(.*?)"',url).group(1))
            merge.append(re.sub("<a.*?>.*?</a>",host,url))
        else:
            merge.append(url)
except:
    traceback.print_exc()

# ========== 抓取 kkzui.com 的节点 ==========
try:
    res = requests.get("https://kkzui.com/jd?orderby=modified",headers=headers)
    article_url = re.search(r'<h2 class="item-heading"><a href="(https://kkzui.com/(.*?)\.html)">20(.*?)号(.*?)个高速免费节点(.*?)免费代理</a></h2>',res.text).groups()[0]

    res = requests.get(article_url,headers=headers)
    sub_url = re.search(r'<p><strong>这是v2订阅地址</strong>：(.*?)</p>',res.text).groups()[0]

    res = requests.get(sub_url,headers=headers)
    merge += str(base64.b64decode(res.text.encode()),'utf-8').strip().replace('\r\n','\n').split('\n')
except:
    traceback.print_exc()

# ========== 抓取 JACKUSR2089/v2ray-subscribed 的节点 ==========
try:
    res = requests.get("https://api.github.com/repos/JACKUSR2089/v2ray-subscribed/contents").json()
    subs = {}

    for file in res:
        name = re.match(r"(\d+)(-|\.)(\d+)(-|\.)(\d+)",file['name'])
        if name:
            subs[name.group()] = int(name.groups()[0])*10000+int(name.groups()[2])*100+int(name.groups()[4])

    subs = sorted(subs.items(),key=lambda k:k[1])
    sub_url = "https://raw.githubusercontent.com/JACKUSR2089/v2ray-subscribed/master/"+subs[-1][0]

    res = requests.get(sub_url)
    merge += str(base64.b64decode(res.text.encode()),'utf-8').strip().replace('\r\n','\n').split('\n')
except:
    traceback.print_exc()

# ========== 写出文件 ==========
txt = ''
for url in set(merge):
    txt = txt + url + '\n'

with open("list_raw.txt",'w') as f:
    f.write(txt)
with open("list.txt",'w') as f:
    b64txt = base64.b64encode(txt.encode())
    f.write(str(b64txt,'utf-8'))
