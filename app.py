from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


@app.route('/')
def homework():
    return render_template('shopping.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

# 여길 채워나가세요!
    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'number': number_receive,
    }
    db.orders.insert_one(doc)

    return jsonify({'result': 'success', 'msg':'주문이 완료되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orders.find({}, {'_id': False}))
    print(orders)
# 여길 채워나가세요!
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=2000, debug=True)