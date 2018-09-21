#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2018/09/20 17:11
# @Author: zhangxiaolin
# @File: getscnauthor.py
import os
import subprocess
import sys
from tempfile import TemporaryFile, NamedTemporaryFile

if __name__ == '__main__':
    filePath = 'Author.txt'
    cmd = r'svn log --quiet  '
    email = 'gszh.cn'

    if len(sys.argv) > 1 :
        if len(sys.argv[1].strip()) > 0:
            email = sys.argv[1].strip()
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    stdout = p.stdout.read()
    r = p.wait()
    p.stdout.close()
    cmdResutl = stdout.decode("utf8", "ignore").strip('\n').split('\n')
    _index1 = -1
    _index2 = -1
    authorList = []
    for line in cmdResutl:
        _index1 = line.find('|')
        _index2 = line.find('|', _index1 + 1)
        if _index1 > 0 & _index1 < _index2:
            line = line[_index1 + 1:_index2].strip()
            if line not in authorList:
                authorList.append(line)

    with open(filePath, 'w+') as f:
        if len(authorList) > 0:
            for line in authorList:
                f.write('{0} = {0} <{0}@{1}>{2}'.format(line, email, '\n'))
        else:
            f.write('当前目录非svn根目录（1、本程序请放在.svn目录下2、网络出现故障）！')
    # # 用文件描述符来操作临时文件
    # f = TemporaryFile()
    # f.write(cmdResutl.)
    # f.seek(0)
    # line = f.readline()
    # while line:
    # line = f.readline()
    # ntf = NamedTemporaryFile()
    # # 返回文件路径
    # ntf.name
