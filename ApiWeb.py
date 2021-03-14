from flask import Flask
from flask_cors import CORS,cross_origin

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=68)


@app.route('/add', methods=['GET'])
@cross_origin(origin='*')
def hello_word():
    return "xin chao"
