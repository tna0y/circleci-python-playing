from flask import Flask


app = Flask(__name__)

@app.route('/hw')
def hw():
    return 'Hello, World'

@app.route('/hw2')
def hw2():
    return 'Hello, World 2'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)