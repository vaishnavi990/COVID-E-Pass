# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()'''
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = 'rosa'
    return render_template('index.html', title='Welcome', username=name)


if __name__ == '__main__':
    app.run()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
