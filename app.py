from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def stream():
    url = "https://375213f059a3.ngrok-free.app/stream.mp3"  # 改這裡
    headers = {
        'ngrok-skip-browser-warning': '1'  # 用來跳過 Ngrok 防護頁面
    }
    r = requests.get(url, headers=headers, stream=True)
    return Response(r.iter_content(chunk_size=1024), content_type=r.headers['Content-Type'])
