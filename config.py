import os


class Config:
    MYSQL_HOST = os.environ.get('MYSQL_HOST', '192.168.1.127')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '123456')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'meet_product')
    MYSQL_CURSOR_CLASS = 'DictCursor'  # 使用 dict 结构，使得数据可以通过列名字典方式访问
