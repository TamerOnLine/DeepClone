from flask import Flask, request, jsonify
import requests
import os
import json
import hashlib

app = Flask(__name__)

# GitHub API base
GITHUB_API = "https://api.github.com/repos"

# Cache config
CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def get_cache_path(repo_url):
    """Return cache file path based on hash of the repo URL"""
    hash_name = hashlib.md5(repo_url.encode()).hexdigest()
    return os.path.join(CACHE_DIR, f"{hash_name}.json")

def load_from_cache(repo_url):
    path = get_cache_path(repo_url)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_to_cache(repo_url, data):
    path = get_cache_path(repo_url)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def fetch_files_from_github(user, repo, path=""):
    url = f"{GITHUB_API}/{user}/{repo}/contents/{path}"
    response = requests.get(url)

    if response.status_code != 200:
        return None, response.status_code, response.text

    content = response.json()
    files_data = {}

    for item in content:
        if item['type'] == 'file':
            file_content = requests.get(item['download_url']).text
            files_data[item['path']] = file_content
        elif item['type'] == 'dir':
            sub_files, _, _ = fetch_files_from_github(user, repo, item['path'])
            files_data.update(sub_files)

    return files_data, 200, "OK"

@app.route("/fetch", methods=["POST"])
def fetch_repo():
    data = request.get_json()
    repo_url = data.get("repo")

    if not repo_url or "github.com" not in repo_url:
        return jsonify({"error": "Invalid GitHub URL"}), 400

    # ✅ check cache
    cached = load_from_cache(repo_url)
    if cached:
        print(f"✅ Loaded from cache: {repo_url}")
        return jsonify(cached)

    try:
        parts = repo_url.replace("https://github.com/", "").strip("/").split("/")
        user, repo = parts[0], parts[1]
        subpath = "/".join(parts[2:]) if len(parts) > 2 else ""

        files_data, code, msg = fetch_files_from_github(user, repo, subpath)

        if code != 200:
            return jsonify({"error": msg}), code

        result = {"files": files_data}
        save_to_cache(repo_url, result)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5555)
