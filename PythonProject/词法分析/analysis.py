import re

key_word = ["bool", "true", "false", "break", "continue", "goto", "switch", "case",
            "default", "int", "double", "float", "char", "string", "const", "struct",
            "class", "void", "namespace", "if", "else", "while", "for", "return"]

operate_word = ["+", "-", "*", "/", "%", "++", "--", "==",
                "!=", ">=", "<=", "<", ">", "&&", "||", "!", "=", "?"]

border_word = ["(", ")", "{", "}", ";", "<<", ">>", "#", "[", "]"]

name = ["变量", "分界符", "运算符", "关键字"]

result = []  # 存放单词
kind = []  # 存放单词种类


def find(list_name, string, label):
    for word in list_name:
        if re.match(re.escape(word), string):  # 在字符串开头匹配
            result.append(word)  # 将该单词加入输出结果
            kind.append(label)
            string_cut = string[len(word):]  # 去除该单词
            return string_cut, True

    return string, False


def find_var(s, label):
    c = s[0]  # 判断第一个非保留单词，如果出现非法字符直接结束
    if (c.isalpha() or c.isdigit() or c == "_" or c == ".") == False:
        # 变量取名，包括字母、数字、下划线、小数点
        return s, True
    else:
        for i in range(1, len(s)):
            c = s[i]
            if (c.isalpha() or c.isdigit() or c == "_" or c == ".") == False:  # 变量截止
                result.append(s[0:i])  # 将该单词加入输出结果
                kind.append(label)
                string_cut = s[i:]  # 去除该单词
                return string_cut, False
        # 到达句尾
        result.append(s)  # 将该单词加入输出结果
        kind.append(label)
        return "", False


def la(sentence):
# sentence = ''
    # s = sentence.replace(' ', '')  # 去除空格
    # print(s)
    array = sentence.split()
    for s in array:
        global result
        global kind
        kind = []
        result = []

        while len(s) > 0:
            flag = False
            name_error = False
            # 首先使用正则表达式匹配每次开头的字符串
            [s, flag] = find(border_word, s, "分界符")
            if flag:
                continue
            [s, flag] = find(operate_word, s, "操作符")
            if flag:
                continue
            [s, flag] = find(key_word, s, "关键字")
            if flag:
                continue

            # 其次匹配第一个非字母、数字、下划线_的符号，之前作为一整个变量的名称
            [s, name_error] = find_var(s, "变量")
            if name_error:
                print("Error01: 字符 " + s[0:1] + " 是非法字符！")
                break

        if (name_error == False):
            for i in range(0, len(result)):
                if(kind[i] == "变量"):
                    var = result[i]

                    if(len(var) > 7):
                        print("Warning01: 单词" + var + "过长，压缩为：")
                        var = var[0:7]

                    if(var.isdigit()):
                        print(var, "  ", "int常量")
                    elif (var.isalpha()):
                        print(var, "  ", "变量")
                    elif(var.isalnum()):
                        print("Error02: 变量 " + var + " 只能由字母、\"_\"组成！")
                    elif(re.search("\.", var)):
                        pos = re.search("\.", var).start()
                        if(pos == 0 or pos == len(var)-1):
                            print("Error03: 变量 " + var + " 小数点存在异常！")
                        elif(var[0:pos].isdigit() and var[pos+1:].isdigit()):
                            print(var, "  ", "float常量")
                        else:
                            print("Error03: 变量 " + var + " 小数点存在异常！")

                    else:
                        print(var, "  ", "1")
                else:
                    print(result[i], "  ", kind[i])











