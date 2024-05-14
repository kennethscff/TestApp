from flask import Flask, request, jsonify
import git

app = Flask(__name__)

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./TestApp')
    origin = repo.remotes.origin
    repo.create_head('master',
    origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return '', 200

@app.route('/')
def home():
    return "HELLO, World!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello Hi, {name}!"

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.json
    result = sum(data['numbers'])
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
