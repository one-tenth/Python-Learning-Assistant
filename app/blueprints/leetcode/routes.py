import os
from werkzeug.utils import secure_filename # 👈 記得匯入這個
from flask import current_app # 👈 為了取得專案路徑
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import LeetCodeNote
from app import db

# 定義藍圖
leetcode_bp = Blueprint('leetcode', __name__)

# 1. 列表頁：顯示所有筆記
@leetcode_bp.route('/')
def index():
    # 相當於 Django 的 LeetCodeNote.objects.all().order_by('-created_at')
    notes = LeetCodeNote.query.order_by(LeetCodeNote.created_at.desc()).all()
    return render_template('leetcode/index.html', notes=notes)

# 2. 新增頁：處理表單
@leetcode_bp.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        # 從表單抓取資料 (request.form 就像 Django 的 request.POST)
        title = request.form.get('title')
        category = request.form.get('category')
        difficulty = request.form.get('difficulty')
        link = request.form.get('link')
        code = request.form.get('code')
        explanation = request.form.get('explanation')
        image_file = request.files.get('image') # 取得上傳的檔案
        filename = None # 預設是沒有圖片

        if image_file and image_file.filename != '':
            # 1. 確保檔名安全 (例如把 "my photo.jpg" 變成 "my_photo.jpg")
            filename = secure_filename(image_file.filename)
            
            # 2. 設定存檔路徑 (存到 app/static/uploads)
            upload_path = os.path.join(current_app.root_path, 'static', 'uploads')
            
            # 3. 確保資料夾存在 (怕你忘記建資料夾)
            os.makedirs(upload_path, exist_ok=True)
            
            # 4. 存檔
            image_file.save(os.path.join(upload_path, filename))

        # 建立物件
        new_note = LeetCodeNote(
            title=title,
            category=category,
            difficulty=difficulty,
            link=link,
            code=code,
            explanation=explanation,
            image_filename=filename
        )

        # 存入資料庫
        db.session.add(new_note)
        db.session.commit()

        # 新增完成，跳轉回列表頁
        return redirect(url_for('leetcode.index'))

    # 如果是 GET 請求，就顯示表單
    return render_template('leetcode/add.html')

# 3. 詳情頁：看單一篇筆記
@leetcode_bp.route('/<int:id>')
def detail(id):
    # 相當於 Django 的 get_object_or_404
    note = LeetCodeNote.query.get_or_404(id)
    return render_template('leetcode/detail.html', note=note)