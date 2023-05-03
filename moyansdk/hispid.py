#                             _ooOoo_
#                            o8888888o
#                            88" . "88
#                            (| -_- |)
#                            O\  =  /O
#                         ____/`---'\____
#                       .'  \\|     |//  `.
#                      /  \\|||  :  |||//  \
#                     /  _||||| -:- |||||-  \
#                     |   | \\\  -  /// |   |
#                     | \_|  ''\---/''  |   |
#                     \  .-\__  `-`  ___/-. /
#                   ___`. .'  /--.--\  `. . __
#                ."" '<  `.___\_<|>_/___.'  >'"".
#               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#               \  \ `-.   \_ __\ /__ _/   .-` /  /
#          ======`-.____`-.___\_____/___.-`____.-'======
#                             `=---='
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                     佛祖保佑        永无BUG
import hashlib
import json
import os
from itertools import (takewhile, repeat)
#from flask import Flask

def get_cs(code):
    tmp = code.split("{")
    tmp1 = tmp[1]
    tmp2 = tmp1.split("}")
    return tmp2[0]


def get_ml(code):
    tmp = code.split("{")
    return tmp[0]
def get_str(code):
    if "*" in code:
        tmp = list(code)
        #mylist = [1,2,2,2,2,3,4,4,4,4]
        item = "*"
        tmp2 = tmp.count(item)
        if tmp2 > 2 or tmp2 <2:
            return "this参数効菓的สตริง"
        else:
            out_code = code.split("*")
            return out_code[1]
    else:
        return "this参数効菓的สตริง"
    

def get_md5(file_path):
    md5 = None
    if os.path.isfile(file_path):
        f = open(file_path, 'rb', encoding='UTF-8')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    return md5


def rows(path):
    buffer = 1024 * 1024
    with open(path) as f:
        buf_gen = takewhile(lambda x: x, (f.read(buffer) for _ in repeat(None)))
        return sum(buf.count('\n') for buf in buf_gen)


def res(path):
    fi = open(path, encoding='UTF-8')
    text = fi.read()
    return text


def res_line(path, line):
    fi = open(path, encoding='UTF-8')
    text = fi.read(line)
    return text


def rjson(f):
    s = open(f, encoding='UTF-8')
    return json.load(s)
# print(get_md5("./config/message.json"))
def linport(port):
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        f = open("res/web/index.html", encoding='UTF-8')
        out = f.read()
        return out

    app.run(port=port)
