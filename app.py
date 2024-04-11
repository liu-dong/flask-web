import datetime

from flask import Flask, render_template

from api import api
from extension import db, cors

app = Flask(__name__)

# 数据库配置，根据实际情况进行修改
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@192.168.1.127:3306/meet_product'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

db.init_app(app)
cors.init_app(app)


@api.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hello')
def hello():  # put application's code here
    return '您好，世界！'


@app.route('/index')
def index():  # put application's code here
    time = datetime.date.today()
    return render_template("index.html", var=time)


app.register_blueprint(api, url_prefix="/api")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
