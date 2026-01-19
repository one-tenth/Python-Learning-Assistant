# app/models.py
from app.extensions import db
from datetime import datetime

class LeetCodeNote(db.Model):
    __tablename__ = 'leetcode_notes'

    id = db.Column(db.Integer, primary_key=True)
    # 👇 檢查這一行！是不是拼錯了？或是沒存檔？
    title = db.Column(db.String(100), nullable=False)
    image_filename = db.Column(db.String(100), nullable=True)
    category = db.Column(db.String(50), default='Uncategorized')
    difficulty = db.Column(db.String(20))
    link = db.Column(db.String(200))
    code = db.Column(db.Text)
    explanation = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<LeetCodeNote {self.title}>'