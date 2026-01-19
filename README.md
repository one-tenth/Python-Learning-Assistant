# 🐍 Python Learning Assistant (with Local AI)

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-green?style=for-the-badge&logo=flask&logoColor=white)
![Ollama](https://img.shields.io/badge/AI-Llama%203.1-orange?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap%205-purple?style=for-the-badge&logo=bootstrap&logoColor=white)

> **"Learning by Teaching"**
>
> 一個結合 **Flask** 網頁框架與 **Local LLM (Llama 3.1)** 的個人學習知識庫。除了紀錄 LeetCode 刷題筆記，還內建 AI 助教隨時解釋程式碼。

---

## 📸 專案預覽 (Screenshots)

![Dashboard Screenshot](https://via.placeholder.com/800x400?text=Please+Upload+Your+Screenshot+Here)

---

## ✨ 核心功能 (Features)

* **📚 LeetCode 筆記系統**：
    * 支援 CRUD (新增、讀取、修改、刪除) 刷題紀錄。
    * 紀錄題目難度 (Easy/Medium/Hard) 與演算法分類 (Two Pointers, DP...)。
    * **圖片上傳功能**：可上傳手繪解題思路圖，輔助學習。
* **🤖 AI 隨身助教 (AI Tutor)**：
    * 整合 **Ollama** 本地端模型接口。
    * 在筆記詳情頁可一鍵呼叫 **Llama 3.1**，自動解釋複雜的 Python 程式碼或演算法邏輯。
* **🎨 現代化介面**：
    * 使用 Bootstrap 5 響應式設計 (RWD)。
    * 程式碼語法高亮 (Syntax Highlighting)。

---

## 🛠️ 技術棧 (Tech Stack)

| Category | Technology |
| :--- | :--- |
| **Backend** | Python, Flask, Flask-SQLAlchemy |
| **Frontend** | HTML5, Jinja2, Bootstrap 5, JavaScript (Fetch API) |
| **Database** | SQLite (輕量化單一檔案資料庫) |
| **AI / LLM** | Ollama (Running Llama 3.1 locally) |

---

## 🚀 快速開始 (Quick Start)

### 1. 環境準備
請確保你的電腦已安裝：
* [Python 3.8+](https://www.python.org/)
* [Ollama](https://ollama.com/) (用於運行 AI 模型)

### 2. 下載專案
```bash
git clone [https://github.com/one-tenth/Python-Learning-Assistant.git](https://github.com/one-tenth/Python-Learning-Assistant.git)
cd Python-Learning-Assistant
```

### 3. 安裝依賴套件

建議使用虛擬環境 (Virtual Environment) 以避免套件衝突。

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**安裝需求套件：**
```bash
pip install -r requirements.txt
```

### 4. 設定 AI 模型 (Ollama)
請在終端機執行以下指令，確保已下載 Llama 3.1 模型並保持服務開啟：

```bash
ollama pull llama3.1
ollama serve
```

### 5. 啟動網站
回到專案目錄執行：
```bash
python run.py
```
啟動後，請在瀏覽器打開：`http://127.0.0.1:5000`

---

## 📂 專案結構 (Project Structure)

```text
my_flask_project/
├── app/
│   ├── blueprints/      # 功能模組 (Main, LeetCode)
│   ├── static/          # CSS, JS, Uploads (Images)
│   ├── templates/       # HTML 頁面 (Jinja2)
│   ├── models.py        # 資料庫模型 (SQLAlchemy)
│   └── __init__.py      # App 工廠模式入口
├── run.py               # 啟動腳本
└── requirements.txt     # 套件清單
```

---

## 📝 開發日誌 & 未來規劃 (Roadmap)

- [x] 完成基礎 CRUD 功能
- [x] 整合 Ollama Local API
- [x] 實作圖片上傳功能
- [ ] 加入全文搜尋功能 (Full-text Search)
- [ ] 實作使用者登入系統 (User Authentication)
- [ ] 優化 AI 回應速度 (Streaming Response)

---

## 📧 Contact

如果你對這個專案有興趣，歡迎聯絡我！

* **GitHub**: [one-tenth](https://github.com/one-tenth)