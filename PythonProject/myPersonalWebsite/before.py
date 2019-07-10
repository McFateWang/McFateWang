'''
# from flask import Flask #代入类
# app = Flask(__name__)#创建一个实例
#
# @app.route('/')#什么样的URL触发
# def index():
#     return 'index page'
#
# @app.route('/hello')
# def hello_world():
#         return 'hello world!'
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username#打印用户信息
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#
# if __name__=='__main__':
#     app.run()
#     #app.run(host='0.0.0.0')#监听公网IP，使服务器公开可用
'''

from flask import Flask, request, render_template

app = Flask(__name__)  # 创建一个实例


@app.route('/', methods=['GET', 'POST'])  # get获取页面信息 post发布新信息
def home():
    print("connected!")
    # return render_template('home.html')
    return "connected!"


@app.route('/signin', methods=['GET'])  # 登录界面，给客户端返回输入用户密码界面
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])  # 接收客户端发送的信息，得到输入的用户密码
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '123456':
        print("OK!")
        # return render_template('signin-ok.html', username=username)
        return "you are sign in correctly"
    else:
        return render_template('form.html', message='Bad username or password', username=username)


@app.route('/message', methods=['GET'])  # 发送系统记录到的人员进出信息
def mes():

    # id = request.form['id']
    # place = request.form['place']
    # time = request.form['time']
    # in_out = request.form['in_out']
    # # 判断人员进出
    # if in_out == 0:
    #     pos = 'in_door'
    # else:
    #     pos = 'out_door'
    # print('get message as :' + id + ' ' + place + '' + time + '' + pos)
    print(id)
    return render_template('mes.html')
    # return "message accepted"


@app.route('/message', methods=['POST'])  # 发送系统记录到的人员进出信息
def message():
    id = request.form['id']
    place = request.form['place']
    time = request.form['time']
    in_out = request.form['in_out']
    # 判断人员进出
    if in_out == 0:
        pos = 'in_door'
    else:
        pos = 'out_door'
    print('get message as :' + id + ' ' + place + ' ' + time + '' + pos)
    return "message accepted"


@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    feature = request.form['feature']
    print(name, feature)
    return 'Hello World!'

# flask默认开启的网站是本地的127.0.0.1:5000
# 现在把已经有的本机访问改成局域网访问
# app.run(host=’0.0.0.0’,port=8080)
# port可以不配置，默认还是5000，如果修改则是修改后的内容
#
# 局域网访问采用 主机IP地址+端口号
#
# 在windows下搭建后需要开启防火墙的入站规则，指定端口号


if __name__ == '__main__':  # 打开局域网，URL需要主机cmd-config-查看id地址，客户端内填入对应url地址
    #app.run(port=8888)
    #app.run(host='0.0.0.0', port=8888)
    app.run()


