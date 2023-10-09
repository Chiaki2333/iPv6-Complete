#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

#ipv6_1 = 'fe80::e493:3995:5571:be'


def ipv6_1_2(ipv6_1):
    #check ipv6
    ff = False
    if ipv6_1[0]=='[' and ipv6_1[-1]==']':ff = True
    ipv6_1 = ipv6_1.replace('[','').replace(']','')
    for i in ipv6_1:
        if i == ':' or i=='[' or i==']':continue
        if not (ord(i)>=ord('0') and ord(i)<=ord('9')) and not (ord(i)>=ord('A') and ord(i)<=ord('F')) and not (ord(i)>=ord('a') and ord(i)<=ord('f')):
            return 'Your IPv6 is wrong!'
    if ipv6_1.count('::') >= 2 or ipv6_1.count(':') >= 8 or len(ipv6_1)>39:
        return 'Your IPv6 is wrong!'
    
    if '::' in ipv6_1:
        ipv6_1 = ipv6_1.replace('::',':'*(9-ipv6_1.count(':')))
    flag = 0
    tmp = ''
    ipv6_2 = ''
    for i in ipv6_1:
        if i != ':':
            flag += 1
            tmp += i
        elif i == ':':
            ipv6_2 += ('0'*(4-flag)+tmp+':')
            tmp = ''
            flag = 0
    ipv6_2 += ('0'*(4-flag)+tmp)
    if ff:ipv6_2 = '[' + ipv6_2 + ']'
    return ipv6_2    

def print_help():
    print("""Usage: python """ + sys.argv[0] + """ [ipv6/Options]

Options:
  -h, --help            Show basic help message and exit

Example: 
  python """ + sys.argv[0] + """ fe80::e493:3995:5571:be
  python """ + sys.argv[0] + """""")







if __name__== "__main__":
    if '-h' in sys.argv:
        print_help()
    elif len(sys.argv) >= 2:
        print(ipv6_1_2(sys.argv[1]))
    else:
        string = ''
        while 'exit' != string and 'quit' != string:
            string = input("[Input your IPv6]")
            print(ipv6_1_2(string))