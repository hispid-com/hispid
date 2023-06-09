#                            _ooOoo_
#                           o8888888o
#                            88" . "88
#                             (| -_- |)
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
import moyansdk.hispid as sdk
from plugin_manager import Plugin_init
import data
#初始化插件
plu = Plugin_init('plugins')
message = sdk.rjson("config.json")
def main(code,line,codes,path):
   #将所有字符转换为小写
    command = code.lower()
    if "{" not in command:
        print("The line '{}' at line {} is not the correct HISPID command".format(codes[line+1],line+1))
    elif "{" in command:
        info = {
            "line":line,
            "file":path,
            "primitive":code,
            "all_var":data.vars,
            "all_list":data.lists,
            "all_dict":data.dicts
        }
        cs = sdk.get_cs(command)
        ml = sdk.get_ml(command)
        # print(cs)
        # print(ml)
        if ml == "help":
            f = open("res/help/{}.txt".format(message["language"]), encoding='UTF-8')
            print(f.read())
        elif ml == "copyright":
            f = open("res/copyright", encoding='UTF-8')
            print(f.read())
        elif ml == "license":
            f = open("LICENSE", encoding='UTF-8')
            print(f.read())
        elif ml == "exit":
            exit()
        elif ml == "pycode":
            csStr = sdk.get_str(cs)
            #print(csStr)
            if csStr == "this参数効菓的สตริง":
                print("In the {} line, these: {} are not valid strings".format(line+1,codes[line]))
            else:
                exec(csStr)
        else:
            plu.apply_all_plugins_on_value(ml,cs,info)
