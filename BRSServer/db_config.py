# 安装mysql5.6   8.x    安装界面化操作工具Navicate Heidsql
# 1、pip install pymysql
# 2、pip install Flask-SQLAlchemy


# --------------------配置数据库---------------------
from flask_sqlalchemy  import SQLAlchemy
from flask import Flask
app = Flask(__name__)
# 数据库配置                                               用户名：密码@ip：port/数据库名字
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/bookrecommendationsystem'

# 数据库操作对象
db_init = SQLAlchemy(app)

