from flask import Flask, request, send_from_directory
from flask import render_template

from random import randint

app = Flask(__name__, static_url_path='')
from specials import *

# This displays a plotly.js graph
@app.route('/plot/')
def boxplot():
    return render_template('boxplot.html')

# This displays a plotly.js graph
@app.route('/plotBubble/')
def boxplotBubble():
    return render_template('boxplotBubble.html')

@app.route('/csv/<path:path>')
def send_csv(path):
    return send_from_directory('csv', path)


# This passes a function to a template
@app.route('/specials/')
def specials():
    return render_template('specials.html',
                           special=get_special())

# This shows how to pass parameters to a template
@app.route('/lucky/')
def lucky():
    lucky_number = randint(1, 99)
    return render_template('lucky.html',
                           lucky_num=lucky_number)


@app.route('/test/')
def test_page():
    return "This is a test page."

# @app.route('/process/<proc_name>/')
# def process_page(proc_name):
#     return render_template('process.html',
#                            process_name=proc_name)

@app.route('/process/<proc_name>/')
def process_page(proc_name):
    return render_template('process.html',
                           process_name=proc_name)



if __name__ == '__main__':
    app.run()
