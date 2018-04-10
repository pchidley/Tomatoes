from bottle import route, run, template

@route('/')
@route('/hello')
@route('/hello/<name>')
def greet(name='Stranger'):
  return template('Hello {{name}}'', name=name)
  
run(host='0.0.0.0', port=8080)

