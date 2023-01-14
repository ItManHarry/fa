from flask import Flask, render_template, url_for, redirect, make_response
from markupsafe import escape
def create_app():
    app = Flask('com')
    @app.route('/hi')
    def hi():
        return '<h1>Flask again 222!!!</h1>'
    @app.route('/projects/')
    def projects():
        return '<h1>Projects</h1>'
    @app.route('/hello/<name>')
    def hello(name):
        return f'hello, {escape(name)}!'
    @app.route('/post/<int:num>')
    def post(num):
        return '<h1>Number is : '+str(num)+'</h1>'
    @app.route('/path/<path:sub_path>')
    def path(sub_path):
        return f'Sub path is : {escape(sub_path)}!'
    @app.route('/about')
    def about():
        return '</h1>This is about page...</h1>'
    @app.route('/home')
    def home():
        resp = make_response(render_template('home.html', name='Harry'))
        resp.set_cookie('f2_name', 'Harry')
        return resp
    @app.route('/json')
    def json():
        return {
            'name': 'Jack',
            'age': 40,
            'gender': 'M',
            'hobbies': ['Watching Movies', 'Playing Ping-Pong', 'Singing']
        }
    @app.route('/')
    def index():
        return redirect(url_for('home'))
    return app