from flask import Flask, request, render_template
# 创建一个实例
app = Flask(__name__)


# 使用装饰器修饰路由，该程序被部署在服务器上并绑定域名
# 客户端输入网址时将触发函数
# 客户端接收到的返回值被称为响应，web浏览器接收到HTML文档
@app.route('/')
def index():
    return '<h1>hello world!!!<h1>'


# 测试界面，获取GET请求后返回form文件给客户端
@app.route('/test', methods=['GET'])
def test_get():
    return render_template('form.html')


# 测试界面，获取POST请求后处理request的表单信息，
@app.route('/test', methods=['POST'])
def test_post():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '123456':
        print("OK!")
        return "成功登录！！！"
    else:
        return render_template('form.html', message='用户名或者密码错误！', username=username)


# 获取网站
@app.route('/McFate', methods=['GET'])
def my_fun():
    return render_template('McFate.html')


# 获取网站
@app.route('/flask_post_form', methods=['POST'])
def my_fun_2():
    guest_name = request.form['wj-name']
    guest_sex = request.form['sex']
    guest_word = request.form['wj-word']
    print('get message as :')
    print(guest_name)
    print(guest_sex)
    print(guest_word)
    return render_template('after_post.html')


# 程序运行入口,启动flask集成的web服务
if __name__ == '__main__':
    app.run(debug=True)