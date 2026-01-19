# app/blueprints/main/routes.py
from flask import Blueprint, render_template

# 定義藍圖，名稱叫 'main'
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    # 假資料，之後會從資料庫撈
    posts = [
        {'title': 'Flask 學習筆記', 'summary': '這是我的第一篇 Flask 文章'},
        {'title': 'LeetCode Two Sum', 'summary': '使用 Hash Map 解題'}
    ]
    return render_template('index.html', posts=posts)