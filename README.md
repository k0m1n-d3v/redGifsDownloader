[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-%E2%98%95%EF%B8%8F-yellow?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://coff.ee/k0m1n)

# 🚀 RedGifs Downloader

Automated, user-friendly tool for downloading videos from RedGifs user pages.  
Bypasses bot detection, works in Docker, and is easy to configure.

---

## ✨ Features

- 🤖 **Bypasses bot detection** (undetected-chromedriver)
- 🐳 **Docker-ready** (one command to run)
- ⚡ **Fast & automatic** (scrolls, collects, downloads)
- 🛠️ **Configurable** (URL, download path, scrolls)
- 📦 **No browser needed on your machine**
- 📁 **Saves videos to your chosen folder**

---

## 🟢 Quick Start

### 1. **Docker (recommended)**
```bash
# Build the image (first time only)
docker build -t redgifs-downloader .

# Create a folder for downloads
mkdir downloads

# Run the app (replace the URL if you want)
docker run --rm -v $(pwd)/downloads:/downloads redgifs-downloader \
  --url "https://www.redgifs.com/users/your-username" \
  --download-path /downloads
```

### 2. **Local (Python)**
```bash
pip install -r requirements.txt
python main.py --url "https://www.redgifs.com/users/your-username" --download-path "./downloads"
```

---

## ⚙️ How it works

1. **Connects to RedGifs** and scrolls through the user’s page.
2. **Collects all video links** automatically.
3. **Downloads videos** to your chosen folder using `yt-dlp`.
4. **Bypasses anti-bot protection** using undetected-chromedriver.

---

## 💡 Why use this tool?

- No manual clicking or copying links
- Works on any system (thanks to Docker)
- Avoids RedGifs bot detection
- Fully automatic and configurable
- Open-source and easy to extend

---

## ☕ Support my work

If you find this project useful,  
please consider supporting me:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-%E2%98%95%EF%B8%8F-yellow?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://coff.ee/k0m1n)

---

**Made with ❤️ by k0m1n-d3v** 