from flask import Flask,url_for,redirect,request
app = Flask(__name__)
#默认情况下，Flask路由响应GET请求。但是，可以通过为route()装饰器提供方法参数来更改此首选项。

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))
#<variable_name> ， 这个部分将会作为命名参数传递到你的函数。规则可以用 <converter:variable_name> 指定一个可选的转换器。

@app.route('/success/<name>')
def success(name):
   return 'welcome %s for get' % name

@app.route('/postweb')
def login_post():
    return "this is post"
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('login_post'))

if __name__ == '__main__':
    app.debug = True#启用了调试支持，服务器会在代码修改后自动重新载入，并在发生 错误时提供一个相当有用的调试器
    app.run(host='0.0.0.0')#修改调用 run() 的方法使你的服务器公开可用