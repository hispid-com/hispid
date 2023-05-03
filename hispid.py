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

import sys

import core
import moyansdk.hispid as sdk
#读取消息文件
message = sdk.rjson("config.json")

#定义入口程序
def main(comms="NUll"):
    #将消息写入变量
    tmp = message["out_text"]
    oss = message["OS"]
    bit = message["bit"]
    jg= message["jg"]
    ver = message["version"]
    pre = message["pre"]
    #打印版本号等
    print(tmp.format(ver, bit, jg ,pre, oss))
    #进入死循环
    while True:
        code = input(">>>")
        #调用core.main函数处理命令
        codes = []
        codes.append("")
        codes.append(code)
        core.main(code,0,codes,"[In memory]")

#以文件运行hispid
def fileed(path):
    line = 0
    if ".his" in path:
        #打开his文件
        f = open(path,"r")
        file_data = f.read()
        temp = file_data.split(":;\n")
        flie_command = temp
        print(flie_command)
        for i in flie_command:
            if i == "":
                continue
            else:
                core.main(i,line,flie_command,path)
                line = line+1
    else:
        print("this flie is not HIS file.")

#获取命令行参数
command_line_parameters = sys.argv
#判断命令行参数
if "-f" in command_line_parameters:
    #获取-f的索引
    findex = command_line_parameters.index("-f")
    #获取-f的参数
    filepath = command_line_parameters[findex + 1]
    #调用filepath函数运行
    fileed(filepath)
    # print(filepath)
#获取参数长度
elif len(command_line_parameters) < 2:
    main()
elif "-v" in command_line_parameters:
    #读取消息并输出
    print(message["version"])
elif "-h" in command_line_parameters:
    f = open("res/help/chinese.txt", encoding='UTF-8')
    print(f.read())
elif "-nm" in command_line_parameters:
    clindex = command_line_parameters.index("-nm")
    port = int(command_line_parameters[clindex + 1])
    sdk.linport(port)
