import datetime
import json

from flask import Flask, render_template, request, jsonify

from models import db, Product, result

app = Flask(__name__)

# 数据库配置，根据实际情况进行修改
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@192.168.1.127:3306/meet_product'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hello')
def hello():  # put application's code here
    return '您好，世界！'


@app.route('/index')
def index():  # put application's code here
    time = datetime.date.today()
    return render_template("index.html", var=time)


@app.before_first_request
def create_tables():
    db.create_all()


# 增加新商品
@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(
        id=data['id'],
        product_name=data['product_name'],
        product_code=data['product_code'],
        product_type=data['product_type'],
        product_status=data['product_status'],
        product_description=data.get('product_description', ''),
        image_url=data.get('image_url', ''),
        selling_price=data['selling_price'],
        remark=data.get('remark', ''),
        delete_status=data.get('delete_status', 0),
        create_time=datetime.now(),
        create_user_id=data.get('create_user_id', '')
    )
    product.add()
    return jsonify({"message": "Product added successfully"}), 201


# 删除商品
@app.route('/product/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        product.delete()
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"message": "Product not found"}), 404


# 更新商品
@app.route('/product/<string:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if product:
        data = request.get_json()
        product.product_name = data.get('product_name', product.product_name)
        product.product_code = data.get('product_code', product.product_code)
        product.product_type = data.get('product_type', product.product_type)
        product.product_status = data.get('product_status', product.product_status)
        product.product_description = data.get('product_description', product.product_description)
        product.image_url = data.get('image_url', product.image_url)
        product.selling_price = data.get('selling_price', product.selling_price)
        product.remark = data.get('remark', product.remark)
        product.delete_status = data.get('delete_status', product.delete_status)
        product.update_time = datetime.now()
        product.update_user_id = data.get('update_user_id', product.update_user_id)
        product.update()
        return jsonify({"message": "Product updated successfully"}), 200
    return jsonify({"message": "Product not found"}), 404


# 查询商品列表
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_data = []
    for product in products:
        json_data = json.dumps(product.to_dict())
        products_data.append(json_data)
    return jsonify(result(products_data, 200, "查询成功"))


if __name__ == '__main__':
    app.run()