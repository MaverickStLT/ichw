#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Li Tao"
__pkuid__  = "1700011605"
__email__  = "1700011605@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    s2=lines
    s1=lines.lower()
    #全部变为小写
    s=''
    for i in range(len(s1)):
        if s1[i]=='.' or s1[i]==',' or s1[i]=='"'or s1[i]=='!' or s1[i]=='?' or s1[i]=='('or s1[i]==')' or s1[i]=='—' or s1[i]=='_' or (s1[i]=='-' and s1[i+1]=='-') or s1[i]==';':
            s=s+' '
        else:
            s=s+s1[i]
    #去掉标点符号
    t=s.split()
    l=len(t)
    dic={}
    i=0
    n=0
    m=''
    while l>0:
        m=t[0]
        n=0
        while i<l:
            if t[i]==m:
                n=n+1
                del t[i]
                l=l-1
            else:
                i=i+1
        i=0
        dic[m]=n
        #将一行中单词个数统计到一个字典里。
    dic1=sorted(dic.items(), key=lambda dic:dic[1],reverse=True)
    #排序
    for i in range (topn):
        print (dic1[i])


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)