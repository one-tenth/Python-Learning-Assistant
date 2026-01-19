import os
from flask import Flask
from app.extensions import db  # 1. 從我們剛建好的 extensions 匯入 db

def create_app():
    app = Flask(__name__)

    # --- 👇 這是你剛剛缺少的設定區塊 (像是 Django 的 settings.py) ---
    
    # 設定密鑰 (Session 用)
    app.config['SECRET_KEY'] = 'dev-key-for-learning'
    
    # 設定資料庫連線字串 (這是錯誤的主因！)
    # 這行意思是：在專案目錄下建立一個叫 database.db 的 SQLite 檔案
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, '..', 'database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    
    # 關閉追蹤修改 (節省記憶體，通常都設 False)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- 👆 設定結束 ---

    # 2. 初始化資料庫
    db.init_app(app) 

    # 3. 建立資料庫表 (如果不存在的話)
    with app.app_context():
        from app import models  # 匯入 models 讓 SQLAlchemy 知道表結構
        db.create_all()         # 這行會自動產生 database.db 檔案

    # 4. 註冊藍圖
    from app.blueprints.main.routes import main_bp
    from app.blueprints.leetcode.routes import leetcode_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(leetcode_bp, url_prefix='/leetcode')

    return app