from bottle import route, run, template

@route('/')
def index():
  ""Home Page""
  info = {'title':GOL,
           'content': 'Switch Data'
           }
  return template('/root/python/index3.tpl', info)           
           
@route('/hello')
@route('/hello/<name>')
def greet(name='Stranger'):
  return template('Hello {{name}}'', name=name)
  
run(host='0.0.0.0', port=8080)

