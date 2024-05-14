from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

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
