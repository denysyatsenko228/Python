from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Denys Yatsenko TZ-82'

if __name__ == '__main__':
app.run('0.0.0.0')
