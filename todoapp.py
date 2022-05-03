from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)
todo_list = []


@app.route('/clear', methods=['POST'])
def clear():
    del todo_list[:]
    return redirect('/')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    task = request.form["task"]
    email = request.form["email"]
    priority = request.form["priority"]
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        todo_list.append((task, email, priority))

    priorities = ['high', 'medium', 'low']
    if priority not in priorities:
        return redirect('/')

    tup = ((task, email, priority)) #list
    todo_list.append(tup)
    return redirect('/')


@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

if __name__ == '__main__':
    # website I used to help show code in browser:
    # https://programmierfrage.com/items/error-the-browser-or-proxy-sent-a-request-that-this-server-could-not-understa
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='127.0.0.1', port=port, debug=True)
