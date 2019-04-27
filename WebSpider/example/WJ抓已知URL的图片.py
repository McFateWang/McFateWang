# -*- coding:utf-8 -*-
#  author: WangJie
import requests
import os
import time
import random
# from bs4 import BeautifulSoup


# 获取HTML源码
def my_get_html(url):
    # 伪装成浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=20)
        print("成功获取~~", url)
    except:
        print("发出的GET请求失败！！", url)
        os.system("pause")

    return resp


# 建立URL列表
def my_get_url(base_url, page_1, page_last, img_flag, name_rule):
    url_list = []
    if name_rule == 'two':
        for page in range(page_1, page_last + 1):
            if page < 10:
                one_url = base_url + img_flag + '0' + str(page) + '.jpg'  # 10以下有前缀0X
            else:
                one_url = base_url + img_flag + str(page) + '.jpg'
            url_list.append(one_url)

    elif name_rule == 'three':
        for page in range(page_1, page_last + 1):
            if page < 10:
                one_url = base_url + img_flag + '00' + str(page) + '.jpg'  # 10以下有前缀00X
            elif page < 100:
                one_url = base_url + img_flag + '0' + str(page) + '.jpg'
            else:
                one_url = base_url + img_flag + str(page) + '.jpg'
            url_list.append(one_url)

    return url_list


# 指定图片要存放的地点
def my_dir(my_main_dic, path):
    if_exist = os.path.exists(os.path.join(my_main_dic, path))
    # 如果不存在
    if not if_exist:
        print('创建新文件夹 ', path)
        # 创建文件夹
        os.makedirs(os.path.join(my_main_dic, path))
        # 切换到创建的文件夹
        os.chdir(os.path.join(my_main_dic, path))
        return True
    # 如果存在了就返回False
    else:
        print(path, ' 文件夹已经存在')
        os.chdir(os.path.join(my_main_dic, path))
        return False

# 对URL下载指定图片
def my_download_img(base_url, page_1, page_last, img_flag, name_rule):
    url_list = my_get_url(base_url, page_1, page_last, img_flag, name_rule)
    file_num = page_1
    for url in url_list:
        time.sleep(2 + random.random())  # 每个页面间隔2.x秒获取
        #time.sleep(2)  # 每个页面间隔2.x秒获取
        filename = str(file_num) + '.jpg'
        # filename = url.split('/')[-1]
        with open(filename, 'wb') as f:
            try:
                f.write(my_get_html(url).content)
                print('抓取成功 ', filename)
            except:
                print('抓取失败 ', filename)
        file_num += 1


# 爬虫主函数
def my_main():
    # 指定存放的文件夹
    my_main_dic = "C:/mytools/my_py_pic/"
    my_dir(my_main_dic, '[水龙敬]学园5')
    # 指定下载的URL
    base_url = 'http://pm.weakcn.com/lifanacgup/papapa/20170111/1/'
    page_first = 1
    page_num = 23
    img_flag = 'tt'  # 图片前缀（每个都不一样）
    # 下载图片
    my_download_img(base_url, page_first, page_num, img_flag, 'two')  # 最后一项是命名规则

# 已完成
# 'http://pm.weakcn.com/uploadfile/gx02/180728/dd01.jpg', 240, '[一弘]精灵妹子单行本'
# 'http://pm.weakcn.com/lifanacgup/papapa/20180620/15/000.jpg', 206, '[越中]异世界穿越'
# http://lf.weakcn.com/hcomic/1019/7/000.jpg 269 [水龙敬]观念ZERO
# 'http://pm.weakcn.com/lifanacgup/papapa/20180620/16/000.jpg', 42, '[sian]勇者战败']
# http://pm.weakcn.com/lifanacgup/papapa/20170110/4/001.jpg 53 [水龙敬]学园4

# 未完成
# http://pm.weakcn.com/lifanacgup/papapa/20170111/1/001.jpg 23 [水龙敬]学园5
# http://pm.weakcn.com/lifanacgup/papapa/20170208/1/001.jpg 58 [水龙敬]学园6
# http://pm.weakcn.com/lifanacgup/papapa/20170209/1/001.jpg 39 [水龙敬]学园9
# http://pm.weakcn.com/lifanacgup/papapa/20170315/1/000.jpg 23 [水龙敬]学园8
# http://pm.weakcn.com/lifanacgup/papapa/20170517/2/000.jpg 209 [水龙敬]MC学院
# http://pm.weakcn.com/lifanacgup/papapa/20170704/1/000.jpg 23 [水龙敬]水星
# http://pm.weakcn.com/lifanacgup/papapa/20170216/2/000.jpg 39 [水龙敬]一起来乐园
# http://pm.weakcn.com/lifanacgup/papapa/20180209/2/000.jpg 43 [水龙敬]一起来乐园番外

# 'http://pm.weakcn.com/uploadfile/gx02/180809/tt03.jpg', 198, [CG]合宿免许可
# 'http://pm.weakcn.com/uploadfile/gx02/180813/dd01.jpg', 196, '[池上真上]性转'
# 'http://pm.weakcn.com/uploadfile/gx02/180813/aa01.jpg', 213, '[旧日]NTR'
# 'http://pm.weakcn.com/uploadfile/gx02/180811/gg01.jpg', 199, '[]干妹妹'
#




if __name__ == '__main__':
    # 计时
    t1 = time.time()
    # 调用函数
    my_main()
    # 输出时间
    print("\n使用时间 ", time.time() - t1, " 秒")