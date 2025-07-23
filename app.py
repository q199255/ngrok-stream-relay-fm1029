from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def stream():
    url = "https://c07354e309ad.ngrok-free.app/stream.mp3"  # 改這裡
    headers = {
        'ngrok-skip-browser-warning': '1'  # 用來跳過 Ngrok 防護頁面
    }
    r = requests.get(url, headers=headers, stream=True)
    return Response(r.iter_content(chunk_size=1024), content_type=r.headers['Content-Type'])
