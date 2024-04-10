from extension import db


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.String(36), primary_key=True, default='wait_sale', comment='主键id')
    product_name = db.Column(db.String(50), nullable=False, comment='商品名称')
    product_code = db.Column(db.String(10), nullable=False, comment='商品编号')
    product_type = db.Column(db.SmallInteger, default=0, comment='商品类型（0：其他、1：书籍、2：电子、3：服装）')
    product_status = db.Column(db.String(20), comment='商品状态（on_sale：在售，sold_out：下架）')
    product_description = db.Column(db.String(2000), comment='商品说明')
    image_url = db.Column(db.String(255), comment='商品图片地址')
    selling_price = db.Column(db.Numeric(10, 2), comment='出售价格')
    remark = db.Column(db.String(1000), comment='备注')
    delete_status = db.Column(db.Integer, default=0, comment='是否删除 0：否、1：是')
    create_time = db.Column(db.DateTime, nullable=False, comment='创建时间')
    create_user_id = db.Column(db.String(36), comment='创建人id')
    update_time = db.Column(db.DateTime, comment='修改时间')
    update_user_id = db.Column(db.String(36), comment='修改人id')

    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "product_name": self.product_name,
            "product_code": self.product_code,
            "product_type": self.product_type,
            "product_status": self.product_status,
            "product_description": self.product_description,
            "image_url": self.image_url,
        }

