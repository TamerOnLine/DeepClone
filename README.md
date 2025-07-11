# 🚀 DeepClone

**DeepClone** is a lightweight Flask-based server that allows you to fetch all files from a public GitHub repository (including nested folders) via a simple POST API request.

---

## 🧠 Concept

Instead of running `git clone`, DeepClone uses the GitHub REST API to recursively fetch the repository content and return it as a JSON object containing file paths and their contents.

---

## 📦 Usage

### ▶️ Start the Server

```bash
python setup.py
```

Or directly:

```bash
python app.py
```

The server will run at:  
`http://127.0.0.1:5555`

---

### 📬 Endpoint `/fetch`

#### ✅ Method: `POST`  
#### 🧾 URL: `/fetch`

#### 📥 Body (JSON):
```json
{
  "repo": "https://github.com/USERNAME/REPO_NAME"
}
```

> You can also target a subfolder:  
> `"repo": "https://github.com/USERNAME/REPO_NAME/tree/main/path/to/subfolder"`

#### 📤 Response (Success):
```json
{
  "files": {
    "README.md": "# README content",
    "src/app.py": "print('Hello')"
  }
}
```

#### ❌ Response (Error):
```json
{
  "error": "Invalid GitHub URL"
}
```

---

## 🧰 Requirements

- Python 3.12+
- Flask
- requests

### 📄 Install:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Project Files

```
DeepClone/
│
├── app.py                # Main script (Flask API)
├── setup.py              # Auto setup (venv + run)
├── setup-config.json     # Customizable configuration
├── requirements.txt      # Dependencies
└── .gitignore            # Ignore venv and temp files
```

---

## 🛡️ Legality

✅ **Yes** – As long as the repository is public and you’re not requesting private or protected content, this complies with GitHub’s public API terms.

---

## 💡 Future Ideas

- Support private repositories using GitHub tokens
- Add a web interface to browse content
- Cache fetched repos for further analysis
- Allow selective file downloads

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it with attribution.  
Feel free to explore and build upon it!

---

## 👨‍💻 About the Author

🎯 **Tamer OnLine – Developer & Architect**  
A dedicated software engineer and educator with a focus on building multilingual, modular, and open-source applications using Python, Flask, and PostgreSQL.

🔹 Founder of **Flask University** – an initiative to create real-world, open-source Flask projects  
🔹 Creator of [@mystrotamer](https://www.youtube.com/@mystrotamer) – a YouTube channel sharing tech, tutorials, and Pi Network insights  
🔹 Passionate about helping developers learn by building, one milestone at a time

Connect or contribute:

[![GitHub](https://img.shields.io/badge/GitHub-TamerOnLine-181717?style=flat&logo=github)](https://github.com/TamerOnLine)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/tameronline/)  
[![YouTube](https://img.shields.io/badge/YouTube-mystrotamer-red?style=flat&logo=youtube)](https://www.youtube.com/@mystrotamer)

---


