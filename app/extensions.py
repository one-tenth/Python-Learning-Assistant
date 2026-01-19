# app/extensions.py
from flask_sqlalchemy import SQLAlchemy

# 這裡先建立一個空的 SQLAlchemy 物件，之後再用 init_app 綁定
db = SQLAlchemy()