from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myDb                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('card.html')

## API 역할을 하는 부분
@app.route('/myCollection', methods=['POST'])
def write_myCollection():
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route('/myCollection', methods=['GET'])
def read_myCollection():
    word = list(db.myCollection.find({},{'_id':0}))
    return jsonify({'result':'success', 'msg': '이 요청은 GET!', 'words_list':word })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)